from . import Entity


class Runner(Entity):
    """A runner represents a single combination of horse, jockey and trainer competing in a race"""
    
    @property
    def has_expired(self):
        """Expire runners that were last updated prior to the start time of the associated race"""

        return self['updated_at'] < self.race['start_time'] or super(Runner, self).has_expired

    @property
    def race(self):
        """Return the race in which this runner is competing"""

        return self.get_cached_property('race', self.provider.get_race_by_runner, self)

    def is_equivalent_to(self, other_runner):
        """This runner is equivalent to other_runner if both have the same race_id and number"""

        return self['race_id'] == other_runner['race_id'] and self['number'] == other_runner['number']
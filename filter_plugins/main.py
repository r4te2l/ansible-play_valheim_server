#!/usr/bin/env python3
class FilterModule(object):
    def filters(self):
        return {
            'valheim_old_backups': self.valheim_old_backups
        }

    def valheim_old_backups(self, backup_files, max_backups):
        sorted_files = sorted(backup_files, key=lambda k: k['mtime'])
        return sorted_files[:(0 - max_backups)]

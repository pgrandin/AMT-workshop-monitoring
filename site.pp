class { 'grafana': 
  cfg => {
    'auth.anonymous' => {
      enabled => true,
    },
  },

}

class { 'graphite':

  gr_storage_schemas        => [
    {
      name       => 'carbon',
      pattern    => '^carbon\.',
      retentions => '1m:90d'
    },
    {
      name       => 'default',
      pattern    => '.*',
      retentions => '30s:6h,1m:1d,5m:2y',
    }
  ],
}


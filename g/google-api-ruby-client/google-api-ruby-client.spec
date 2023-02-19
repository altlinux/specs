Name:          google-api-ruby-client
Version:       20221017
Release:       alt1.1
Summary:       REST client for Google APIs
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/googleapis/google-api-ruby-client
Vcs:           https://github.com/googleapis/google-api-ruby-client.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 1.17
BuildRequires: gem(rake) >= 12.0
BuildRequires: gem(rspec) >= 3.9 gem(rspec) < 4
BuildRequires: gem(opencensus) >= 0.5 gem(opencensus) < 1
BuildRequires: gem(yard) >= 0.9.25 gem(yard) < 1
BuildRequires: gem(redcarpet) >= 3.5 gem(redcarpet) < 4
BuildRequires: gem(bundler) >= 1.7
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.1 gem(rspec) < 4
BuildRequires: gem(json_spec) >= 1.1 gem(json_spec) < 2
BuildRequires: gem(webmock) >= 3.0 gem(webmock) < 4
BuildRequires: gem(simplecov) >= 0.12 gem(simplecov) < 1
BuildRequires: gem(coveralls) >= 0.8 gem(coveralls) < 1
BuildRequires: gem(rubocop) >= 0.49.0 gem(rubocop) < 2
BuildRequires: gem(launchy) >= 2.4 gem(launchy) < 3
BuildRequires: gem(dotenv) >= 2.0 gem(dotenv) < 3
BuildRequires: gem(fakefs) >= 1.0 gem(fakefs) < 2
BuildRequires: gem(google-id-token) >= 1.3 gem(google-id-token) < 2
BuildRequires: gem(os) >= 0.9 gem(os) < 2
BuildRequires: gem(rmail) >= 1.1 gem(rmail) < 2
BuildRequires: gem(redis) >= 3.2 gem(redis) < 6
BuildRequires: gem(logging) >= 2.2 gem(logging) < 3
BuildRequires: gem(opencensus) >= 0.4 gem(opencensus) < 1
BuildRequires: gem(httparty) >= 0
BuildRequires: gem(gems) >= 1.2 gem(gems) < 2
BuildRequires: gem(yard) >= 0.9.11 gem(yard) < 1
BuildRequires: gem(redcarpet) >= 3.2 gem(redcarpet) < 4
BuildRequires: gem(github-markup) >= 1.3 gem(github-markup) < 5
BuildRequires: gem(pry-doc) >= 0.8 gem(pry-doc) < 2
BuildRequires: gem(pry-byebug) >= 3.2 gem(pry-byebug) < 4
BuildRequires: gem(representable) >= 3.0 gem(representable) < 4
BuildRequires: gem(retriable) >= 2.0 gem(retriable) < 4.a
BuildRequires: gem(addressable) >= 2.5.1 gem(addressable) < 3
BuildRequires: gem(mini_mime) >= 1.0 gem(mini_mime) < 2
BuildRequires: gem(googleauth) >= 0.16.2 gem(googleauth) < 2.a
BuildRequires: gem(httpclient) >= 2.8.1 gem(httpclient) < 3.a
BuildRequires: gem(rexml) >= 0
BuildRequires: gem(webrick) >= 0
BuildRequires: gem(activesupport) >= 5.0
BuildRequires: gem(thor) >= 0.20 gem(thor) < 2.a
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency os >= 1.1.0,os < 2
%ruby_use_gem_dependency github-markup >= 4.0.0,github-markup < 5
%ruby_use_gem_dependency pry-doc >= 1.1.0,pry-doc < 2
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency redis >= 5.0,redis < 6
%ruby_ignore_names web,cli,/beta[5-9],/beta[0-3],/alpha,/apis-[aefhj-lnoqrt-z],/apis-g[a-df-z],/apis-d[a-hj-mo-z],/apis-c[a-kmnp-z],/genomics,/dia,/dig,/display,/apis-cloud[a-ps-z],/classroom,/apis-cloudr.*v[23],/apis-co[a-lops-z],google-api-ruby-client
Provides:      ruby-google-api-ruby-client


%description
This repository contains a set of simple client libraries for various Google
APIs. These libraries are generated automatically from Discovery Documents, and
the code generator is also hosted here in this repository.

Each client provides:

* A client object that connects to the HTTP/JSON REST endpoint for the
service.
* Ruby objects for data structures related to the service.
* Integration with the googleauth gem for authentication using OAuth, API keys,
and service accounts.
* Control of retry, pagination, and timeouts.

These client libraries are officially supported by Google, and are updated
regularly to track changes to the service. However, many Google services,
especially Google Cloud Platform services such as Cloud Storage, Pub/Sub, and
BigQuery, may provide a more modern client that is easier to use and more
performant. See the section below titled "Which client should I use?" for more
information.


%package       -n gem-google-apis-baremetalsolution-v1
Version:       0.13.0
Release:       alt1.1
Summary:       Simple REST client for Bare Metal Solution API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-baremetalsolution_v1) = 0.13.0

%description   -n gem-google-apis-baremetalsolution-v1
This is the simple REST client for Bare Metal Solution API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Bare Metal Solution API, but
note that some services may provide a separate modern client that is easier to
use.


%package       -n gem-google-apis-baremetalsolution-v1-doc
Version:       0.13.0
Release:       alt1.1
Summary:       Simple REST client for Bare Metal Solution API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-baremetalsolution_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-baremetalsolution_v1) = 0.13.0

%description   -n gem-google-apis-baremetalsolution-v1-doc
Simple REST client for Bare Metal Solution API V1 documentation files.

This is the simple REST client for Bare Metal Solution API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Bare Metal Solution API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-baremetalsolution-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-baremetalsolution_v1.


%package       -n gem-google-apis-baremetalsolution-v1-devel
Version:       0.13.0
Release:       alt1.1
Summary:       Simple REST client for Bare Metal Solution API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-baremetalsolution_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-baremetalsolution_v1) = 0.13.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-baremetalsolution-v1-devel
Simple REST client for Bare Metal Solution API V1 development package.

This is the simple REST client for Bare Metal Solution API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Bare Metal Solution API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-baremetalsolution-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-baremetalsolution_v1.


%package       -n gem-google-apis-baremetalsolution-v2
Version:       0.24.0
Release:       alt1.1
Summary:       Simple REST client for Bare Metal Solution API V2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-baremetalsolution_v2) = 0.24.0

%description   -n gem-google-apis-baremetalsolution-v2
This is the simple REST client for Bare Metal Solution API V2. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Bare Metal Solution API, but
note that some services may provide a separate modern client that is easier to
use.


%package       -n gem-google-apis-baremetalsolution-v2-doc
Version:       0.24.0
Release:       alt1.1
Summary:       Simple REST client for Bare Metal Solution API V2 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-baremetalsolution_v2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-baremetalsolution_v2) = 0.24.0

%description   -n gem-google-apis-baremetalsolution-v2-doc
Simple REST client for Bare Metal Solution API V2 documentation files.

This is the simple REST client for Bare Metal Solution API V2. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Bare Metal Solution API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-baremetalsolution-v2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-baremetalsolution_v2.


%package       -n gem-google-apis-baremetalsolution-v2-devel
Version:       0.24.0
Release:       alt1.1
Summary:       Simple REST client for Bare Metal Solution API V2 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-baremetalsolution_v2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-baremetalsolution_v2) = 0.24.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-baremetalsolution-v2-devel
Simple REST client for Bare Metal Solution API V2 development package.

This is the simple REST client for Bare Metal Solution API V2. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Bare Metal Solution API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-baremetalsolution-v2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-baremetalsolution_v2.


%package       -n gem-google-apis-beyondcorp-v1
Version:       0.7.0
Release:       alt1.1
Summary:       Simple REST client for BeyondCorp API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-beyondcorp_v1) = 0.7.0

%description   -n gem-google-apis-beyondcorp-v1
This is the simple REST client for BeyondCorp API V1. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the BeyondCorp API, but note that some services may
provide a separate modern client that is easier to use.


%package       -n gem-google-apis-beyondcorp-v1-doc
Version:       0.7.0
Release:       alt1.1
Summary:       Simple REST client for BeyondCorp API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-beyondcorp_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-beyondcorp_v1) = 0.7.0

%description   -n gem-google-apis-beyondcorp-v1-doc
Simple REST client for BeyondCorp API V1 documentation files.

This is the simple REST client for BeyondCorp API V1. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the BeyondCorp API, but note that some services may
provide a separate modern client that is easier to use.

%description   -n gem-google-apis-beyondcorp-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-beyondcorp_v1.


%package       -n gem-google-apis-beyondcorp-v1-devel
Version:       0.7.0
Release:       alt1.1
Summary:       Simple REST client for BeyondCorp API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-beyondcorp_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-beyondcorp_v1) = 0.7.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-beyondcorp-v1-devel
Simple REST client for BeyondCorp API V1 development package.

This is the simple REST client for BeyondCorp API V1. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the BeyondCorp API, but note that some services may
provide a separate modern client that is easier to use.

%description   -n gem-google-apis-beyondcorp-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-beyondcorp_v1.


%package       -n gem-google-apis-bigquery-v2
Version:       0.42.0
Release:       alt1.1
Summary:       REST client for Google APIs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-bigquery_v2) = 0.42.0

%description   -n gem-google-apis-bigquery-v2
REST client for Google APIs.


%package       -n gem-google-apis-bigquery-v2-doc
Version:       0.42.0
Release:       alt1.1
Summary:       REST client for Google APIs documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-bigquery_v2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-bigquery_v2) = 0.42.0

%description   -n gem-google-apis-bigquery-v2-doc
REST client for Google APIs documentation files.

%description   -n gem-google-apis-bigquery-v2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-bigquery_v2.


%package       -n gem-google-apis-bigquery-v2-devel
Version:       0.42.0
Release:       alt1.1
Summary:       REST client for Google APIs development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-bigquery_v2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-bigquery_v2) = 0.42.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-bigquery-v2-devel
REST client for Google APIs development package.

%description   -n gem-google-apis-bigquery-v2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-bigquery_v2.


%package       -n gem-google-apis-bigquerydatatransfer-v1
Version:       0.28.0
Release:       alt1.1
Summary:       Simple REST client for BigQuery Data Transfer API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-bigquerydatatransfer_v1) = 0.28.0

%description   -n gem-google-apis-bigquerydatatransfer-v1
This is the simple REST client for BigQuery Data Transfer API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the BigQuery Data Transfer API,
but note that some services may provide a separate modern client that is easier
to use.


%package       -n gem-google-apis-bigquerydatatransfer-v1-doc
Version:       0.28.0
Release:       alt1.1
Summary:       Simple REST client for BigQuery Data Transfer API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-bigquerydatatransfer_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-bigquerydatatransfer_v1) = 0.28.0

%description   -n gem-google-apis-bigquerydatatransfer-v1-doc
Simple REST client for BigQuery Data Transfer API V1 documentation files.

This is the simple REST client for BigQuery Data Transfer API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the BigQuery Data Transfer API,
but note that some services may provide a separate modern client that is easier
to use.

%description   -n gem-google-apis-bigquerydatatransfer-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-bigquerydatatransfer_v1.


%package       -n gem-google-apis-bigquerydatatransfer-v1-devel
Version:       0.28.0
Release:       alt1.1
Summary:       Simple REST client for BigQuery Data Transfer API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-bigquerydatatransfer_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-bigquerydatatransfer_v1) = 0.28.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-bigquerydatatransfer-v1-devel
Simple REST client for BigQuery Data Transfer API V1 development package.

This is the simple REST client for BigQuery Data Transfer API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the BigQuery Data Transfer API,
but note that some services may provide a separate modern client that is easier
to use.

%description   -n gem-google-apis-bigquerydatatransfer-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-bigquerydatatransfer_v1.


%package       -n gem-google-apis-bigqueryreservation-v1
Version:       0.21.0
Release:       alt1.1
Summary:       Simple REST client for BigQuery Reservation API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-bigqueryreservation_v1) = 0.21.0

%description   -n gem-google-apis-bigqueryreservation-v1
This is the simple REST client for BigQuery Reservation API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the BigQuery Reservation API, but
note that some services may provide a separate modern client that is easier to
use.


%package       -n gem-google-apis-bigqueryreservation-v1-doc
Version:       0.21.0
Release:       alt1.1
Summary:       Simple REST client for BigQuery Reservation API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-bigqueryreservation_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-bigqueryreservation_v1) = 0.21.0

%description   -n gem-google-apis-bigqueryreservation-v1-doc
Simple REST client for BigQuery Reservation API V1 documentation files.

This is the simple REST client for BigQuery Reservation API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the BigQuery Reservation API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-bigqueryreservation-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-bigqueryreservation_v1.


%package       -n gem-google-apis-bigqueryreservation-v1-devel
Version:       0.21.0
Release:       alt1.1
Summary:       Simple REST client for BigQuery Reservation API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-bigqueryreservation_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-bigqueryreservation_v1) = 0.21.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-bigqueryreservation-v1-devel
Simple REST client for BigQuery Reservation API V1 development package.

This is the simple REST client for BigQuery Reservation API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the BigQuery Reservation API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-bigqueryreservation-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-bigqueryreservation_v1.


%package       -n gem-google-apis-bigtableadmin-v1
Version:       0.11.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Bigtable Admin API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.4 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-bigtableadmin_v1) = 0.11.0

%description   -n gem-google-apis-bigtableadmin-v1
This is the simple REST client for Cloud Bigtable Admin API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Cloud Bigtable Admin API, but
note that some services may provide a separate modern client that is easier to
use.


%package       -n gem-google-apis-bigtableadmin-v1-doc
Version:       0.11.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Bigtable Admin API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-bigtableadmin_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-bigtableadmin_v1) = 0.11.0

%description   -n gem-google-apis-bigtableadmin-v1-doc
Simple REST client for Cloud Bigtable Admin API V1 documentation files.

This is the simple REST client for Cloud Bigtable Admin API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Cloud Bigtable Admin API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-bigtableadmin-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-bigtableadmin_v1.


%package       -n gem-google-apis-bigtableadmin-v1-devel
Version:       0.11.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Bigtable Admin API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-bigtableadmin_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-bigtableadmin_v1) = 0.11.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-bigtableadmin-v1-devel
Simple REST client for Cloud Bigtable Admin API V1 development package.

This is the simple REST client for Cloud Bigtable Admin API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Cloud Bigtable Admin API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-bigtableadmin-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-bigtableadmin_v1.


%package       -n gem-google-apis-bigtableadmin-v2
Version:       0.29.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Bigtable Admin API V2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-bigtableadmin_v2) = 0.29.0

%description   -n gem-google-apis-bigtableadmin-v2
This is the simple REST client for Cloud Bigtable Admin API V2. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Cloud Bigtable Admin API, but
note that some services may provide a separate modern client that is easier to
use.


%package       -n gem-google-apis-bigtableadmin-v2-doc
Version:       0.29.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Bigtable Admin API V2 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-bigtableadmin_v2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-bigtableadmin_v2) = 0.29.0

%description   -n gem-google-apis-bigtableadmin-v2-doc
Simple REST client for Cloud Bigtable Admin API V2 documentation files.

This is the simple REST client for Cloud Bigtable Admin API V2. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Cloud Bigtable Admin API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-bigtableadmin-v2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-bigtableadmin_v2.


%package       -n gem-google-apis-bigtableadmin-v2-devel
Version:       0.29.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Bigtable Admin API V2 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-bigtableadmin_v2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-bigtableadmin_v2) = 0.29.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-bigtableadmin-v2-devel
Simple REST client for Cloud Bigtable Admin API V2 development package.

This is the simple REST client for Cloud Bigtable Admin API V2. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Cloud Bigtable Admin API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-bigtableadmin-v2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-bigtableadmin_v2.


%package       -n gem-google-apis-billingbudgets-v1
Version:       0.21.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Billing Budget API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-billingbudgets_v1) = 0.21.0

%description   -n gem-google-apis-billingbudgets-v1
This is the simple REST client for Cloud Billing Budget API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Cloud Billing Budget API, but
note that some services may provide a separate modern client that is easier to
use.


%package       -n gem-google-apis-billingbudgets-v1-doc
Version:       0.21.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Billing Budget API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-billingbudgets_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-billingbudgets_v1) = 0.21.0

%description   -n gem-google-apis-billingbudgets-v1-doc
Simple REST client for Cloud Billing Budget API V1 documentation files.

This is the simple REST client for Cloud Billing Budget API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Cloud Billing Budget API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-billingbudgets-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-billingbudgets_v1.


%package       -n gem-google-apis-billingbudgets-v1-devel
Version:       0.21.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Billing Budget API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-billingbudgets_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-billingbudgets_v1) = 0.21.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-billingbudgets-v1-devel
Simple REST client for Cloud Billing Budget API V1 development package.

This is the simple REST client for Cloud Billing Budget API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Cloud Billing Budget API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-billingbudgets-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-billingbudgets_v1.


%package       -n gem-google-apis-binaryauthorization-v1
Version:       0.23.0
Release:       alt1.1
Summary:       Simple REST client for Binary Authorization API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-binaryauthorization_v1) = 0.23.0

%description   -n gem-google-apis-binaryauthorization-v1
This is the simple REST client for Binary Authorization API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Binary Authorization API, but
note that some services may provide a separate modern client that is easier to
use.


%package       -n gem-google-apis-binaryauthorization-v1-doc
Version:       0.23.0
Release:       alt1.1
Summary:       Simple REST client for Binary Authorization API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-binaryauthorization_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-binaryauthorization_v1) = 0.23.0

%description   -n gem-google-apis-binaryauthorization-v1-doc
Simple REST client for Binary Authorization API V1 documentation files.

This is the simple REST client for Binary Authorization API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Binary Authorization API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-binaryauthorization-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-binaryauthorization_v1.


%package       -n gem-google-apis-binaryauthorization-v1-devel
Version:       0.23.0
Release:       alt1.1
Summary:       Simple REST client for Binary Authorization API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-binaryauthorization_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-binaryauthorization_v1) = 0.23.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-binaryauthorization-v1-devel
Simple REST client for Binary Authorization API V1 development package.

This is the simple REST client for Binary Authorization API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Binary Authorization API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-binaryauthorization-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-binaryauthorization_v1.


%package       -n gem-google-apis-blogger-v2
Version:       0.12.0
Release:       alt1.1
Summary:       Simple REST client for Blogger API V2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-blogger_v2) = 0.12.0

%description   -n gem-google-apis-blogger-v2
This is the simple REST client for Blogger API V2. Simple REST clients are Ruby
client libraries that provide access to Google services via their HTTP REST API
endpoints. These libraries are generated and updated automatically based on the
discovery documents published by the service, and they handle most concerns such
as authentication, pagination, retry, timeouts, and logging. You can use this
client to access the Blogger API, but note that some services may provide a
separate modern client that is easier to use.


%package       -n gem-google-apis-blogger-v2-doc
Version:       0.12.0
Release:       alt1.1
Summary:       Simple REST client for Blogger API V2 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-blogger_v2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-blogger_v2) = 0.12.0

%description   -n gem-google-apis-blogger-v2-doc
Simple REST client for Blogger API V2 documentation files.

This is the simple REST client for Blogger API V2. Simple REST clients are Ruby
client libraries that provide access to Google services via their HTTP REST API
endpoints. These libraries are generated and updated automatically based on the
discovery documents published by the service, and they handle most concerns such
as authentication, pagination, retry, timeouts, and logging. You can use this
client to access the Blogger API, but note that some services may provide a
separate modern client that is easier to use.

%description   -n gem-google-apis-blogger-v2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-blogger_v2.


%package       -n gem-google-apis-blogger-v2-devel
Version:       0.12.0
Release:       alt1.1
Summary:       Simple REST client for Blogger API V2 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-blogger_v2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-blogger_v2) = 0.12.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-blogger-v2-devel
Simple REST client for Blogger API V2 development package.

This is the simple REST client for Blogger API V2. Simple REST clients are Ruby
client libraries that provide access to Google services via their HTTP REST API
endpoints. These libraries are generated and updated automatically based on the
discovery documents published by the service, and they handle most concerns such
as authentication, pagination, retry, timeouts, and logging. You can use this
client to access the Blogger API, but note that some services may provide a
separate modern client that is easier to use.

%description   -n gem-google-apis-blogger-v2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-blogger_v2.


%package       -n gem-google-apis-blogger-v3
Version:       0.12.0
Release:       alt1.1
Summary:       Simple REST client for Blogger API V3
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-blogger_v3) = 0.12.0

%description   -n gem-google-apis-blogger-v3
This is the simple REST client for Blogger API V3. Simple REST clients are Ruby
client libraries that provide access to Google services via their HTTP REST API
endpoints. These libraries are generated and updated automatically based on the
discovery documents published by the service, and they handle most concerns such
as authentication, pagination, retry, timeouts, and logging. You can use this
client to access the Blogger API, but note that some services may provide a
separate modern client that is easier to use.


%package       -n gem-google-apis-blogger-v3-doc
Version:       0.12.0
Release:       alt1.1
Summary:       Simple REST client for Blogger API V3 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-blogger_v3
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-blogger_v3) = 0.12.0

%description   -n gem-google-apis-blogger-v3-doc
Simple REST client for Blogger API V3 documentation files.

This is the simple REST client for Blogger API V3. Simple REST clients are Ruby
client libraries that provide access to Google services via their HTTP REST API
endpoints. These libraries are generated and updated automatically based on the
discovery documents published by the service, and they handle most concerns such
as authentication, pagination, retry, timeouts, and logging. You can use this
client to access the Blogger API, but note that some services may provide a
separate modern client that is easier to use.

%description   -n gem-google-apis-blogger-v3-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-blogger_v3.


%package       -n gem-google-apis-blogger-v3-devel
Version:       0.12.0
Release:       alt1.1
Summary:       Simple REST client for Blogger API V3 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-blogger_v3
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-blogger_v3) = 0.12.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-blogger-v3-devel
Simple REST client for Blogger API V3 development package.

This is the simple REST client for Blogger API V3. Simple REST clients are Ruby
client libraries that provide access to Google services via their HTTP REST API
endpoints. These libraries are generated and updated automatically based on the
discovery documents published by the service, and they handle most concerns such
as authentication, pagination, retry, timeouts, and logging. You can use this
client to access the Blogger API, but note that some services may provide a
separate modern client that is easier to use.

%description   -n gem-google-apis-blogger-v3-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-blogger_v3.


%package       -n gem-google-apis-books-v1
Version:       0.12.0
Release:       alt1.1
Summary:       Simple REST client for Books API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-books_v1) = 0.12.0

%description   -n gem-google-apis-books-v1
This is the simple REST client for Books API V1. Simple REST clients are Ruby
client libraries that provide access to Google services via their HTTP REST API
endpoints. These libraries are generated and updated automatically based on the
discovery documents published by the service, and they handle most concerns such
as authentication, pagination, retry, timeouts, and logging. You can use this
client to access the Books API, but note that some services may provide a
separate modern client that is easier to use.


%package       -n gem-google-apis-books-v1-doc
Version:       0.12.0
Release:       alt1.1
Summary:       Simple REST client for Books API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-books_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-books_v1) = 0.12.0

%description   -n gem-google-apis-books-v1-doc
Simple REST client for Books API V1 documentation files.

This is the simple REST client for Books API V1. Simple REST clients are Ruby
client libraries that provide access to Google services via their HTTP REST API
endpoints. These libraries are generated and updated automatically based on the
discovery documents published by the service, and they handle most concerns such
as authentication, pagination, retry, timeouts, and logging. You can use this
client to access the Books API, but note that some services may provide a
separate modern client that is easier to use.

%description   -n gem-google-apis-books-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-books_v1.


%package       -n gem-google-apis-books-v1-devel
Version:       0.12.0
Release:       alt1.1
Summary:       Simple REST client for Books API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-books_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-books_v1) = 0.12.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-books-v1-devel
Simple REST client for Books API V1 development package.

This is the simple REST client for Books API V1. Simple REST clients are Ruby
client libraries that provide access to Google services via their HTTP REST API
endpoints. These libraries are generated and updated automatically based on the
discovery documents published by the service, and they handle most concerns such
as authentication, pagination, retry, timeouts, and logging. You can use this
client to access the Books API, but note that some services may provide a
separate modern client that is easier to use.

%description   -n gem-google-apis-books-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-books_v1.


%package       -n gem-google-apis-businessprofileperformance-v1
Version:       0.4.0
Release:       alt1.1
Summary:       Simple REST client for Business Profile Performance API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-businessprofileperformance_v1) = 0.4.0

%description   -n gem-google-apis-businessprofileperformance-v1
This is the simple REST client for Business Profile Performance API V1. Simple
REST clients are Ruby client libraries that provide access to Google services
via their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Business Profile Performance
API, but note that some services may provide a separate modern client that is
easier to use.


%package       -n gem-google-apis-businessprofileperformance-v1-doc
Version:       0.4.0
Release:       alt1.1
Summary:       Simple REST client for Business Profile Performance API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-businessprofileperformance_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-businessprofileperformance_v1) = 0.4.0

%description   -n gem-google-apis-businessprofileperformance-v1-doc
Simple REST client for Business Profile Performance API V1 documentation
files.

This is the simple REST client for Business Profile Performance API V1. Simple
REST clients are Ruby client libraries that provide access to Google services
via their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Business Profile Performance
API, but note that some services may provide a separate modern client that is
easier to use.

%description   -n gem-google-apis-businessprofileperformance-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-businessprofileperformance_v1.


%package       -n gem-google-apis-businessprofileperformance-v1-devel
Version:       0.4.0
Release:       alt1.1
Summary:       Simple REST client for Business Profile Performance API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-businessprofileperformance_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-businessprofileperformance_v1) = 0.4.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-businessprofileperformance-v1-devel
Simple REST client for Business Profile Performance API V1 development
package.

This is the simple REST client for Business Profile Performance API V1. Simple
REST clients are Ruby client libraries that provide access to Google services
via their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Business Profile Performance
API, but note that some services may provide a separate modern client that is
easier to use.

%description   -n gem-google-apis-businessprofileperformance-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-businessprofileperformance_v1.


%package       -n gem-google-apis-cloudresourcemanager-v1
Version:       0.30.0
Release:       alt1.1
Summary:       REST client for Google APIs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-cloudresourcemanager_v1) = 0.30.0

%description   -n gem-google-apis-cloudresourcemanager-v1
REST client for Google APIs.


%package       -n gem-google-apis-cloudresourcemanager-v1-doc
Version:       0.30.0
Release:       alt1.1
Summary:       REST client for Google APIs documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-cloudresourcemanager_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-cloudresourcemanager_v1) = 0.30.0

%description   -n gem-google-apis-cloudresourcemanager-v1-doc
REST client for Google APIs documentation files.

%description   -n gem-google-apis-cloudresourcemanager-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-cloudresourcemanager_v1.


%package       -n gem-google-apis-cloudresourcemanager-v1-devel
Version:       0.30.0
Release:       alt1.1
Summary:       REST client for Google APIs development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-cloudresourcemanager_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-cloudresourcemanager_v1) = 0.30.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-cloudresourcemanager-v1-devel
REST client for Google APIs development package.

%description   -n gem-google-apis-cloudresourcemanager-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-cloudresourcemanager_v1.


%package       -n gem-google-apis-composer-v1
Version:       0.29.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Composer API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-composer_v1) = 0.29.0

%description   -n gem-google-apis-composer-v1
This is the simple REST client for Cloud Composer API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Cloud Composer API, but note that some
services may provide a separate modern client that is easier to use.


%package       -n gem-google-apis-composer-v1-doc
Version:       0.29.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Composer API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-composer_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-composer_v1) = 0.29.0

%description   -n gem-google-apis-composer-v1-doc
Simple REST client for Cloud Composer API V1 documentation files.

This is the simple REST client for Cloud Composer API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Cloud Composer API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-composer-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-composer_v1.


%package       -n gem-google-apis-composer-v1-devel
Version:       0.29.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Composer API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-composer_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-composer_v1) = 0.29.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-composer-v1-devel
Simple REST client for Cloud Composer API V1 development package.

This is the simple REST client for Cloud Composer API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Cloud Composer API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-composer-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-composer_v1.


%package       -n gem-google-apis-compute-beta
Version:       0.51.0
Release:       alt1.1
Summary:       Simple REST client for Compute Engine API Beta
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-compute_beta) = 0.51.0

%description   -n gem-google-apis-compute-beta
This is the simple REST client for Compute Engine API Beta. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Compute Engine API, but note that some
services may provide a separate modern client that is easier to use.


%package       -n gem-google-apis-compute-beta-doc
Version:       0.51.0
Release:       alt1.1
Summary:       Simple REST client for Compute Engine API Beta documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-compute_beta
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-compute_beta) = 0.51.0

%description   -n gem-google-apis-compute-beta-doc
Simple REST client for Compute Engine API Beta documentation files.

This is the simple REST client for Compute Engine API Beta. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Compute Engine API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-compute-beta-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-compute_beta.


%package       -n gem-google-apis-compute-beta-devel
Version:       0.51.0
Release:       alt1.1
Summary:       Simple REST client for Compute Engine API Beta development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-compute_beta
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-compute_beta) = 0.51.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-compute-beta-devel
Simple REST client for Compute Engine API Beta development package.

This is the simple REST client for Compute Engine API Beta. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Compute Engine API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-compute-beta-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-compute_beta.


%package       -n gem-google-apis-compute-v1
Version:       0.53.0
Release:       alt1.1
Summary:       Simple REST client for Compute Engine API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-compute_v1) = 0.53.0

%description   -n gem-google-apis-compute-v1
This is the simple REST client for Compute Engine API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Compute Engine API, but note that some
services may provide a separate modern client that is easier to use.


%package       -n gem-google-apis-compute-v1-doc
Version:       0.53.0
Release:       alt1.1
Summary:       Simple REST client for Compute Engine API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-compute_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-compute_v1) = 0.53.0

%description   -n gem-google-apis-compute-v1-doc
Simple REST client for Compute Engine API V1 documentation files.

This is the simple REST client for Compute Engine API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Compute Engine API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-compute-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-compute_v1.


%package       -n gem-google-apis-compute-v1-devel
Version:       0.53.0
Release:       alt1.1
Summary:       Simple REST client for Compute Engine API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-compute_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-compute_v1) = 0.53.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-compute-v1-devel
Simple REST client for Compute Engine API V1 development package.

This is the simple REST client for Compute Engine API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Compute Engine API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-compute-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-compute_v1.


%package       -n gem-google-apis-connectors-v1
Version:       0.19.0
Release:       alt1.1
Summary:       Simple REST client for Connectors API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-connectors_v1) = 0.19.0

%description   -n gem-google-apis-connectors-v1
This is the simple REST client for Connectors API V1. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Connectors API, but note that some services may
provide a separate modern client that is easier to use.


%package       -n gem-google-apis-connectors-v1-doc
Version:       0.19.0
Release:       alt1.1
Summary:       Simple REST client for Connectors API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-connectors_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-connectors_v1) = 0.19.0

%description   -n gem-google-apis-connectors-v1-doc
Simple REST client for Connectors API V1 documentation files.

This is the simple REST client for Connectors API V1. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Connectors API, but note that some services may
provide a separate modern client that is easier to use.

%description   -n gem-google-apis-connectors-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-connectors_v1.


%package       -n gem-google-apis-connectors-v1-devel
Version:       0.19.0
Release:       alt1.1
Summary:       Simple REST client for Connectors API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-connectors_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-connectors_v1) = 0.19.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-connectors-v1-devel
Simple REST client for Connectors API V1 development package.

This is the simple REST client for Connectors API V1. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Connectors API, but note that some services may
provide a separate modern client that is easier to use.

%description   -n gem-google-apis-connectors-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-connectors_v1.


%package       -n gem-google-apis-connectors-v2
Version:       0.2.0
Release:       alt1.1
Summary:       Simple REST client for Connectors API V2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-connectors_v2) = 0.2.0

%description   -n gem-google-apis-connectors-v2
This is the simple REST client for Connectors API V2. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Connectors API, but note that some services may
provide a separate modern client that is easier to use.


%package       -n gem-google-apis-connectors-v2-doc
Version:       0.2.0
Release:       alt1.1
Summary:       Simple REST client for Connectors API V2 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-connectors_v2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-connectors_v2) = 0.2.0

%description   -n gem-google-apis-connectors-v2-doc
Simple REST client for Connectors API V2 documentation files.

This is the simple REST client for Connectors API V2. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Connectors API, but note that some services may
provide a separate modern client that is easier to use.

%description   -n gem-google-apis-connectors-v2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-connectors_v2.


%package       -n gem-google-apis-connectors-v2-devel
Version:       0.2.0
Release:       alt1.1
Summary:       Simple REST client for Connectors API V2 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-connectors_v2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-connectors_v2) = 0.2.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-connectors-v2-devel
Simple REST client for Connectors API V2 development package.

This is the simple REST client for Connectors API V2. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Connectors API, but note that some services may
provide a separate modern client that is easier to use.

%description   -n gem-google-apis-connectors-v2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-connectors_v2.


%package       -n gem-google-apis-contactcenterinsights-v1
Version:       0.15.0
Release:       alt1.1
Summary:       Simple REST client for Contact Center AI Insights API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-contactcenterinsights_v1) = 0.15.0

%description   -n gem-google-apis-contactcenterinsights-v1
This is the simple REST client for Contact Center AI Insights API V1. Simple
REST clients are Ruby client libraries that provide access to Google services
via their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Contact Center AI Insights
API, but note that some services may provide a separate modern client that is
easier to use.


%package       -n gem-google-apis-contactcenterinsights-v1-doc
Version:       0.15.0
Release:       alt1.1
Summary:       Simple REST client for Contact Center AI Insights API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-contactcenterinsights_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-contactcenterinsights_v1) = 0.15.0

%description   -n gem-google-apis-contactcenterinsights-v1-doc
Simple REST client for Contact Center AI Insights API V1 documentation
files.

This is the simple REST client for Contact Center AI Insights API V1. Simple
REST clients are Ruby client libraries that provide access to Google services
via their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Contact Center AI Insights
API, but note that some services may provide a separate modern client that is
easier to use.

%description   -n gem-google-apis-contactcenterinsights-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-contactcenterinsights_v1.


%package       -n gem-google-apis-contactcenterinsights-v1-devel
Version:       0.15.0
Release:       alt1.1
Summary:       Simple REST client for Contact Center AI Insights API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-contactcenterinsights_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-contactcenterinsights_v1) = 0.15.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-contactcenterinsights-v1-devel
Simple REST client for Contact Center AI Insights API V1 development
package.

This is the simple REST client for Contact Center AI Insights API V1. Simple
REST clients are Ruby client libraries that provide access to Google services
via their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Contact Center AI Insights
API, but note that some services may provide a separate modern client that is
easier to use.

%description   -n gem-google-apis-contactcenterinsights-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-contactcenterinsights_v1.


%package       -n gem-google-apis-container-v1
Version:       0.37.0
Release:       alt1.1
Summary:       Simple REST client for Kubernetes Engine API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-container_v1) = 0.37.0

%description   -n gem-google-apis-container-v1
This is the simple REST client for Kubernetes Engine API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Kubernetes Engine API, but note that some
services may provide a separate modern client that is easier to use.


%package       -n gem-google-apis-container-v1-doc
Version:       0.37.0
Release:       alt1.1
Summary:       Simple REST client for Kubernetes Engine API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-container_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-container_v1) = 0.37.0

%description   -n gem-google-apis-container-v1-doc
Simple REST client for Kubernetes Engine API V1 documentation files.

This is the simple REST client for Kubernetes Engine API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Kubernetes Engine API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-container-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-container_v1.


%package       -n gem-google-apis-container-v1-devel
Version:       0.37.0
Release:       alt1.1
Summary:       Simple REST client for Kubernetes Engine API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-container_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-container_v1) = 0.37.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-container-v1-devel
Simple REST client for Kubernetes Engine API V1 development package.

This is the simple REST client for Kubernetes Engine API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Kubernetes Engine API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-container-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-container_v1.


%package       -n gem-google-apis-containeranalysis-v1
Version:       0.22.0
Release:       alt1.1
Summary:       Simple REST client for Container Analysis API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-containeranalysis_v1) = 0.22.0

%description   -n gem-google-apis-containeranalysis-v1
This is the simple REST client for Container Analysis API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Container Analysis API, but
note that some services may provide a separate modern client that is easier to
use.


%package       -n gem-google-apis-containeranalysis-v1-doc
Version:       0.22.0
Release:       alt1.1
Summary:       Simple REST client for Container Analysis API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-containeranalysis_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-containeranalysis_v1) = 0.22.0

%description   -n gem-google-apis-containeranalysis-v1-doc
Simple REST client for Container Analysis API V1 documentation files.

This is the simple REST client for Container Analysis API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Container Analysis API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-containeranalysis-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-containeranalysis_v1.


%package       -n gem-google-apis-containeranalysis-v1-devel
Version:       0.22.0
Release:       alt1.1
Summary:       Simple REST client for Container Analysis API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-containeranalysis_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-containeranalysis_v1) = 0.22.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-containeranalysis-v1-devel
Simple REST client for Container Analysis API V1 development package.

This is the simple REST client for Container Analysis API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Container Analysis API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-containeranalysis-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-containeranalysis_v1.


%package       -n gem-google-apis-content-v2
Version:       0.17.0
Release:       alt1.1
Summary:       Simple REST client for Content API for Shopping V2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.4 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-content_v2) = 0.17.0

%description   -n gem-google-apis-content-v2
This is the simple REST client for Content API for Shopping V2. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Content API for Shopping, but
note that some services may provide a separate modern client that is easier to
use.


%package       -n gem-google-apis-content-v2-doc
Version:       0.17.0
Release:       alt1.1
Summary:       Simple REST client for Content API for Shopping V2 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-content_v2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-content_v2) = 0.17.0

%description   -n gem-google-apis-content-v2-doc
Simple REST client for Content API for Shopping V2 documentation files.

This is the simple REST client for Content API for Shopping V2. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Content API for Shopping, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-content-v2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-content_v2.


%package       -n gem-google-apis-content-v2-devel
Version:       0.17.0
Release:       alt1.1
Summary:       Simple REST client for Content API for Shopping V2 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-content_v2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-content_v2) = 0.17.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-content-v2-devel
Simple REST client for Content API for Shopping V2 development package.

This is the simple REST client for Content API for Shopping V2. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Content API for Shopping, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-content-v2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-content_v2.


%package       -n gem-google-apis-content-v2-1
Version:       0.31.0
Release:       alt1.1
Summary:       Simple REST client for Content API for Shopping V2_1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.4 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-content_v2_1) = 0.31.0

%description   -n gem-google-apis-content-v2-1
This is the simple REST client for Content API for Shopping V2_1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Content API for Shopping, but
note that some services may provide a separate modern client that is easier to
use.


%package       -n gem-google-apis-content-v2-1-doc
Version:       0.31.0
Release:       alt1.1
Summary:       Simple REST client for Content API for Shopping V2_1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-content_v2_1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-content_v2_1) = 0.31.0

%description   -n gem-google-apis-content-v2-1-doc
Simple REST client for Content API for Shopping V2_1 documentation files.

This is the simple REST client for Content API for Shopping V2_1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Content API for Shopping, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-content-v2-1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-content_v2_1.


%package       -n gem-google-apis-content-v2-1-devel
Version:       0.31.0
Release:       alt1.1
Summary:       Simple REST client for Content API for Shopping V2_1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-content_v2_1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-content_v2_1) = 0.31.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-content-v2-1-devel
Simple REST client for Content API for Shopping V2_1 development package.

This is the simple REST client for Content API for Shopping V2_1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Content API for Shopping, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-content-v2-1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-content_v2_1.


%package       -n gem-google-apis-contentwarehouse-v1
Version:       0.1.0
Release:       alt1.1
Summary:       Simple REST client for contentwarehouse API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-contentwarehouse_v1) = 0.1.0

%description   -n gem-google-apis-contentwarehouse-v1
This is the simple REST client for contentwarehouse API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the contentwarehouse API, but note that some
services may provide a separate modern client that is easier to use.


%package       -n gem-google-apis-contentwarehouse-v1-doc
Version:       0.1.0
Release:       alt1.1
Summary:       Simple REST client for contentwarehouse API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-contentwarehouse_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-contentwarehouse_v1) = 0.1.0

%description   -n gem-google-apis-contentwarehouse-v1-doc
Simple REST client for contentwarehouse API V1 documentation files.

This is the simple REST client for contentwarehouse API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the contentwarehouse API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-contentwarehouse-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-contentwarehouse_v1.


%package       -n gem-google-apis-contentwarehouse-v1-devel
Version:       0.1.0
Release:       alt1.1
Summary:       Simple REST client for contentwarehouse API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-contentwarehouse_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-contentwarehouse_v1) = 0.1.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-contentwarehouse-v1-devel
Simple REST client for contentwarehouse API V1 development package.

This is the simple REST client for contentwarehouse API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the contentwarehouse API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-contentwarehouse-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-contentwarehouse_v1.


%package       -n gem-google-apis-discovery-v1
Version:       0.12.0
Release:       alt1.1
Summary:       REST client for Google APIs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-discovery_v1) = 0.12.0

%description   -n gem-google-apis-discovery-v1
REST client for Google APIs.


%package       -n gem-google-apis-discovery-v1-doc
Version:       0.12.0
Release:       alt1.1
Summary:       REST client for Google APIs documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-discovery_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-discovery_v1) = 0.12.0

%description   -n gem-google-apis-discovery-v1-doc
REST client for Google APIs documentation files.

%description   -n gem-google-apis-discovery-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-discovery_v1.


%package       -n gem-google-apis-discovery-v1-devel
Version:       0.12.0
Release:       alt1.1
Summary:       REST client for Google APIs development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-discovery_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-discovery_v1) = 0.12.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-discovery-v1-devel
REST client for Google APIs development package.

%description   -n gem-google-apis-discovery-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-discovery_v1.


%package       -n gem-google-apis-dns-v1
Version:       0.28.0
Release:       alt1.1
Summary:       REST client for Google APIs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-dns_v1) = 0.28.0

%description   -n gem-google-apis-dns-v1
REST client for Google APIs.


%package       -n gem-google-apis-dns-v1-doc
Version:       0.28.0
Release:       alt1.1
Summary:       REST client for Google APIs documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-dns_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-dns_v1) = 0.28.0

%description   -n gem-google-apis-dns-v1-doc
REST client for Google APIs documentation files.

%description   -n gem-google-apis-dns-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-dns_v1.


%package       -n gem-google-apis-dns-v1-devel
Version:       0.28.0
Release:       alt1.1
Summary:       REST client for Google APIs development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-dns_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-dns_v1) = 0.28.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-dns-v1-devel
REST client for Google APIs development package.

%description   -n gem-google-apis-dns-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-dns_v1.


%package       -n gem-google-apis-dns-v2
Version:       0.1.0
Release:       alt1.1
Summary:       Simple REST client for Cloud DNS API V2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.4 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-dns_v2) = 0.1.0

%description   -n gem-google-apis-dns-v2
This is the simple REST client for Cloud DNS API V2. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Cloud DNS API, but note that some services may provide
a separate modern client that is easier to use.


%package       -n gem-google-apis-dns-v2-doc
Version:       0.1.0
Release:       alt1.1
Summary:       Simple REST client for Cloud DNS API V2 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-dns_v2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-dns_v2) = 0.1.0

%description   -n gem-google-apis-dns-v2-doc
Simple REST client for Cloud DNS API V2 documentation files.

This is the simple REST client for Cloud DNS API V2. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Cloud DNS API, but note that some services may provide
a separate modern client that is easier to use.

%description   -n gem-google-apis-dns-v2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-dns_v2.


%package       -n gem-google-apis-dns-v2-devel
Version:       0.1.0
Release:       alt1.1
Summary:       Simple REST client for Cloud DNS API V2 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-dns_v2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-dns_v2) = 0.1.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-dns-v2-devel
Simple REST client for Cloud DNS API V2 development package.

This is the simple REST client for Cloud DNS API V2. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Cloud DNS API, but note that some services may provide
a separate modern client that is easier to use.

%description   -n gem-google-apis-dns-v2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-dns_v2.


%package       -n gem-google-apis-iam-v1
Version:       0.35.0
Release:       alt1.1
Summary:       Simple REST client for Identity and Access Management (IAM) API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-iam_v1) = 0.35.0

%description   -n gem-google-apis-iam-v1
This is the simple REST client for Identity and Access Management (IAM) API V1.
Simple REST clients are Ruby client libraries that provide access to Google
services via their HTTP REST API endpoints. These libraries are generated and
updated automatically based on the discovery documents published by the service,
and they handle most concerns such as authentication, pagination, retry,
timeouts, and logging. You can use this client to access the Identity and Access
Management (IAM) API, but note that some services may provide a separate modern
client that is easier to use.


%package       -n gem-google-apis-iam-v1-doc
Version:       0.35.0
Release:       alt1.1
Summary:       Simple REST client for Identity and Access Management (IAM) API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-iam_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-iam_v1) = 0.35.0

%description   -n gem-google-apis-iam-v1-doc
Simple REST client for Identity and Access Management (IAM) API V1 documentation
files.

This is the simple REST client for Identity and Access Management (IAM) API V1.
Simple REST clients are Ruby client libraries that provide access to Google
services via their HTTP REST API endpoints. These libraries are generated and
updated automatically based on the discovery documents published by the service,
and they handle most concerns such as authentication, pagination, retry,
timeouts, and logging. You can use this client to access the Identity and Access
Management (IAM) API, but note that some services may provide a separate modern
client that is easier to use.

%description   -n gem-google-apis-iam-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-iam_v1.


%package       -n gem-google-apis-iam-v1-devel
Version:       0.35.0
Release:       alt1.1
Summary:       Simple REST client for Identity and Access Management (IAM) API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-iam_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-iam_v1) = 0.35.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-iam-v1-devel
Simple REST client for Identity and Access Management (IAM) API V1 development
package.

This is the simple REST client for Identity and Access Management (IAM) API V1.
Simple REST clients are Ruby client libraries that provide access to Google
services via their HTTP REST API endpoints. These libraries are generated and
updated automatically based on the discovery documents published by the service,
and they handle most concerns such as authentication, pagination, retry,
timeouts, and logging. You can use this client to access the Identity and Access
Management (IAM) API, but note that some services may provide a separate modern
client that is easier to use.

%description   -n gem-google-apis-iam-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-iam_v1.


%package       -n gem-google-apis-iam-v2beta
Version:       0.7.0
Release:       alt1.1
Summary:       Simple REST client for Identity and Access Management (IAM) API V2beta
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-iam_v2beta) = 0.7.0

%description   -n gem-google-apis-iam-v2beta
This is the simple REST client for Identity and Access Management (IAM) API
V2beta. Simple REST clients are Ruby client libraries that provide access to
Google services via their HTTP REST API endpoints. These libraries are generated
and updated automatically based on the discovery documents published by the
service, and they handle most concerns such as authentication, pagination,
retry, timeouts, and logging. You can use this client to access the Identity and
Access Management (IAM) API, but note that some services may provide a separate
modern client that is easier to use.


%package       -n gem-google-apis-iam-v2beta-doc
Version:       0.7.0
Release:       alt1.1
Summary:       Simple REST client for Identity and Access Management (IAM) API V2beta documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-iam_v2beta
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-iam_v2beta) = 0.7.0

%description   -n gem-google-apis-iam-v2beta-doc
Simple REST client for Identity and Access Management (IAM) API V2beta
documentation files.

This is the simple REST client for Identity and Access Management (IAM) API
V2beta. Simple REST clients are Ruby client libraries that provide access to
Google services via their HTTP REST API endpoints. These libraries are generated
and updated automatically based on the discovery documents published by the
service, and they handle most concerns such as authentication, pagination,
retry, timeouts, and logging. You can use this client to access the Identity and
Access Management (IAM) API, but note that some services may provide a separate
modern client that is easier to use.

%description   -n gem-google-apis-iam-v2beta-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-iam_v2beta.


%package       -n gem-google-apis-iam-v2beta-devel
Version:       0.7.0
Release:       alt1.1
Summary:       Simple REST client for Identity and Access Management (IAM) API V2beta development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-iam_v2beta
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-iam_v2beta) = 0.7.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-iam-v2beta-devel
Simple REST client for Identity and Access Management (IAM) API V2beta
development package.

This is the simple REST client for Identity and Access Management (IAM) API
V2beta. Simple REST clients are Ruby client libraries that provide access to
Google services via their HTTP REST API endpoints. These libraries are generated
and updated automatically based on the discovery documents published by the
service, and they handle most concerns such as authentication, pagination,
retry, timeouts, and logging. You can use this client to access the Identity and
Access Management (IAM) API, but note that some services may provide a separate
modern client that is easier to use.

%description   -n gem-google-apis-iam-v2beta-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-iam_v2beta.


%package       -n gem-google-apis-iamcredentials-v1
Version:       0.15.0
Release:       alt1.1
Summary:       REST client for Google APIs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-iamcredentials_v1) = 0.15.0

%description   -n gem-google-apis-iamcredentials-v1
REST client for Google APIs.


%package       -n gem-google-apis-iamcredentials-v1-doc
Version:       0.15.0
Release:       alt1.1
Summary:       REST client for Google APIs documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-iamcredentials_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-iamcredentials_v1) = 0.15.0

%description   -n gem-google-apis-iamcredentials-v1-doc
REST client for Google APIs documentation files.

%description   -n gem-google-apis-iamcredentials-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-iamcredentials_v1.


%package       -n gem-google-apis-iamcredentials-v1-devel
Version:       0.15.0
Release:       alt1.1
Summary:       REST client for Google APIs development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-iamcredentials_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-iamcredentials_v1) = 0.15.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-iamcredentials-v1-devel
REST client for Google APIs development package.

%description   -n gem-google-apis-iamcredentials-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-iamcredentials_v1.


%package       -n gem-google-apis-iap-v1
Version:       0.27.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Identity-Aware Proxy API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-iap_v1) = 0.27.0

%description   -n gem-google-apis-iap-v1
This is the simple REST client for Cloud Identity-Aware Proxy API V1. Simple
REST clients are Ruby client libraries that provide access to Google services
via their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Cloud Identity-Aware Proxy
API, but note that some services may provide a separate modern client that is
easier to use.


%package       -n gem-google-apis-iap-v1-doc
Version:       0.27.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Identity-Aware Proxy API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-iap_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-iap_v1) = 0.27.0

%description   -n gem-google-apis-iap-v1-doc
Simple REST client for Cloud Identity-Aware Proxy API V1 documentation
files.

This is the simple REST client for Cloud Identity-Aware Proxy API V1. Simple
REST clients are Ruby client libraries that provide access to Google services
via their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Cloud Identity-Aware Proxy
API, but note that some services may provide a separate modern client that is
easier to use.

%description   -n gem-google-apis-iap-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-iap_v1.


%package       -n gem-google-apis-iap-v1-devel
Version:       0.27.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Identity-Aware Proxy API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-iap_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-iap_v1) = 0.27.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-iap-v1-devel
Simple REST client for Cloud Identity-Aware Proxy API V1 development
package.

This is the simple REST client for Cloud Identity-Aware Proxy API V1. Simple
REST clients are Ruby client libraries that provide access to Google services
via their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Cloud Identity-Aware Proxy
API, but note that some services may provide a separate modern client that is
easier to use.

%description   -n gem-google-apis-iap-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-iap_v1.


%package       -n gem-google-apis-ideahub-v1beta
Version:       0.9.0
Release:       alt1.1
Summary:       Simple REST client for Idea Hub API V1beta
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-ideahub_v1beta) = 0.9.0

%description   -n gem-google-apis-ideahub-v1beta
This is the simple REST client for Idea Hub API V1beta. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Idea Hub API, but note that some services may provide
a separate modern client that is easier to use.


%package       -n gem-google-apis-ideahub-v1beta-doc
Version:       0.9.0
Release:       alt1.1
Summary:       Simple REST client for Idea Hub API V1beta documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-ideahub_v1beta
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-ideahub_v1beta) = 0.9.0

%description   -n gem-google-apis-ideahub-v1beta-doc
Simple REST client for Idea Hub API V1beta documentation files.

This is the simple REST client for Idea Hub API V1beta. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Idea Hub API, but note that some services may provide
a separate modern client that is easier to use.

%description   -n gem-google-apis-ideahub-v1beta-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-ideahub_v1beta.


%package       -n gem-google-apis-ideahub-v1beta-devel
Version:       0.9.0
Release:       alt1.1
Summary:       Simple REST client for Idea Hub API V1beta development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-ideahub_v1beta
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-ideahub_v1beta) = 0.9.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-ideahub-v1beta-devel
Simple REST client for Idea Hub API V1beta development package.

This is the simple REST client for Idea Hub API V1beta. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Idea Hub API, but note that some services may provide
a separate modern client that is easier to use.

%description   -n gem-google-apis-ideahub-v1beta-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-ideahub_v1beta.


%package       -n gem-google-apis-identitytoolkit-v2
Version:       0.3.0
Release:       alt1.1
Summary:       Simple REST client for Identity Toolkit API V2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-identitytoolkit_v2) = 0.3.0

%description   -n gem-google-apis-identitytoolkit-v2
This is the simple REST client for Identity Toolkit API V2. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Identity Toolkit API, but note that some
services may provide a separate modern client that is easier to use.


%package       -n gem-google-apis-identitytoolkit-v2-doc
Version:       0.3.0
Release:       alt1.1
Summary:       Simple REST client for Identity Toolkit API V2 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-identitytoolkit_v2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-identitytoolkit_v2) = 0.3.0

%description   -n gem-google-apis-identitytoolkit-v2-doc
Simple REST client for Identity Toolkit API V2 documentation files.

This is the simple REST client for Identity Toolkit API V2. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Identity Toolkit API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-identitytoolkit-v2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-identitytoolkit_v2.


%package       -n gem-google-apis-identitytoolkit-v2-devel
Version:       0.3.0
Release:       alt1.1
Summary:       Simple REST client for Identity Toolkit API V2 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-identitytoolkit_v2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-identitytoolkit_v2) = 0.3.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-identitytoolkit-v2-devel
Simple REST client for Identity Toolkit API V2 development package.

This is the simple REST client for Identity Toolkit API V2. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Identity Toolkit API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-identitytoolkit-v2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-identitytoolkit_v2.


%package       -n gem-google-apis-identitytoolkit-v3
Version:       0.12.0
Release:       alt1.1
Summary:       Simple REST client for Google Identity Toolkit API V3
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-identitytoolkit_v3) = 0.12.0

%description   -n gem-google-apis-identitytoolkit-v3
This is the simple REST client for Google Identity Toolkit API V3. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Google Identity Toolkit API,
but note that some services may provide a separate modern client that is easier
to use.


%package       -n gem-google-apis-identitytoolkit-v3-doc
Version:       0.12.0
Release:       alt1.1
Summary:       Simple REST client for Google Identity Toolkit API V3 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-identitytoolkit_v3
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-identitytoolkit_v3) = 0.12.0

%description   -n gem-google-apis-identitytoolkit-v3-doc
Simple REST client for Google Identity Toolkit API V3 documentation files.

This is the simple REST client for Google Identity Toolkit API V3. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Google Identity Toolkit API,
but note that some services may provide a separate modern client that is easier
to use.

%description   -n gem-google-apis-identitytoolkit-v3-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-identitytoolkit_v3.


%package       -n gem-google-apis-identitytoolkit-v3-devel
Version:       0.12.0
Release:       alt1.1
Summary:       Simple REST client for Google Identity Toolkit API V3 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-identitytoolkit_v3
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-identitytoolkit_v3) = 0.12.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-identitytoolkit-v3-devel
Simple REST client for Google Identity Toolkit API V3 development package.

This is the simple REST client for Google Identity Toolkit API V3. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Google Identity Toolkit API,
but note that some services may provide a separate modern client that is easier
to use.

%description   -n gem-google-apis-identitytoolkit-v3-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-identitytoolkit_v3.


%package       -n gem-google-apis-ids-v1
Version:       0.8.0
Release:       alt1.1
Summary:       Simple REST client for Cloud IDS API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-ids_v1) = 0.8.0

%description   -n gem-google-apis-ids-v1
This is the simple REST client for Cloud IDS API V1. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Cloud IDS API, but note that some services may provide
a separate modern client that is easier to use.


%package       -n gem-google-apis-ids-v1-doc
Version:       0.8.0
Release:       alt1.1
Summary:       Simple REST client for Cloud IDS API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-ids_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-ids_v1) = 0.8.0

%description   -n gem-google-apis-ids-v1-doc
Simple REST client for Cloud IDS API V1 documentation files.

This is the simple REST client for Cloud IDS API V1. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Cloud IDS API, but note that some services may provide
a separate modern client that is easier to use.

%description   -n gem-google-apis-ids-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-ids_v1.


%package       -n gem-google-apis-ids-v1-devel
Version:       0.8.0
Release:       alt1.1
Summary:       Simple REST client for Cloud IDS API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-ids_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-ids_v1) = 0.8.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-ids-v1-devel
Simple REST client for Cloud IDS API V1 development package.

This is the simple REST client for Cloud IDS API V1. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Cloud IDS API, but note that some services may provide
a separate modern client that is easier to use.

%description   -n gem-google-apis-ids-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-ids_v1.


%package       -n gem-google-apis-indexing-v3
Version:       0.11.0
Release:       alt1.1
Summary:       Simple REST client for Indexing API V3
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-indexing_v3) = 0.11.0

%description   -n gem-google-apis-indexing-v3
This is the simple REST client for Indexing API V3. Simple REST clients are Ruby
client libraries that provide access to Google services via their HTTP REST API
endpoints. These libraries are generated and updated automatically based on the
discovery documents published by the service, and they handle most concerns such
as authentication, pagination, retry, timeouts, and logging. You can use this
client to access the Indexing API, but note that some services may provide a
separate modern client that is easier to use.


%package       -n gem-google-apis-indexing-v3-doc
Version:       0.11.0
Release:       alt1.1
Summary:       Simple REST client for Indexing API V3 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-indexing_v3
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-indexing_v3) = 0.11.0

%description   -n gem-google-apis-indexing-v3-doc
Simple REST client for Indexing API V3 documentation files.

This is the simple REST client for Indexing API V3. Simple REST clients are Ruby
client libraries that provide access to Google services via their HTTP REST API
endpoints. These libraries are generated and updated automatically based on the
discovery documents published by the service, and they handle most concerns such
as authentication, pagination, retry, timeouts, and logging. You can use this
client to access the Indexing API, but note that some services may provide a
separate modern client that is easier to use.

%description   -n gem-google-apis-indexing-v3-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-indexing_v3.


%package       -n gem-google-apis-indexing-v3-devel
Version:       0.11.0
Release:       alt1.1
Summary:       Simple REST client for Indexing API V3 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-indexing_v3
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-indexing_v3) = 0.11.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-indexing-v3-devel
Simple REST client for Indexing API V3 development package.

This is the simple REST client for Indexing API V3. Simple REST clients are Ruby
client libraries that provide access to Google services via their HTTP REST API
endpoints. These libraries are generated and updated automatically based on the
discovery documents published by the service, and they handle most concerns such
as authentication, pagination, retry, timeouts, and logging. You can use this
client to access the Indexing API, but note that some services may provide a
separate modern client that is easier to use.

%description   -n gem-google-apis-indexing-v3-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-indexing_v3.


%package       -n gem-google-apis-managedidentities-v1
Version:       0.25.0
Release:       alt1.1
Summary:       Simple REST client for Managed Service for Microsoft Active Directory API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-managedidentities_v1) = 0.25.0

%description   -n gem-google-apis-managedidentities-v1
This is the simple REST client for Managed Service for Microsoft Active
Directory API V1. Simple REST clients are Ruby client libraries that provide
access to Google services via their HTTP REST API endpoints. These libraries are
generated and updated automatically based on the discovery documents published
by the service, and they handle most concerns such as authentication,
pagination, retry, timeouts, and logging. You can use this client to access the
Managed Service for Microsoft Active Directory API, but note that some services
may provide a separate modern client that is easier to use.


%package       -n gem-google-apis-managedidentities-v1-doc
Version:       0.25.0
Release:       alt1.1
Summary:       Simple REST client for Managed Service for Microsoft Active Directory API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-managedidentities_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-managedidentities_v1) = 0.25.0

%description   -n gem-google-apis-managedidentities-v1-doc
Simple REST client for Managed Service for Microsoft Active Directory API V1
documentation files.

This is the simple REST client for Managed Service for Microsoft Active
Directory API V1. Simple REST clients are Ruby client libraries that provide
access to Google services via their HTTP REST API endpoints. These libraries are
generated and updated automatically based on the discovery documents published
by the service, and they handle most concerns such as authentication,
pagination, retry, timeouts, and logging. You can use this client to access the
Managed Service for Microsoft Active Directory API, but note that some services
may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-managedidentities-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-managedidentities_v1.


%package       -n gem-google-apis-managedidentities-v1-devel
Version:       0.25.0
Release:       alt1.1
Summary:       Simple REST client for Managed Service for Microsoft Active Directory API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-managedidentities_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-managedidentities_v1) = 0.25.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-managedidentities-v1-devel
Simple REST client for Managed Service for Microsoft Active Directory API V1
development package.

This is the simple REST client for Managed Service for Microsoft Active
Directory API V1. Simple REST clients are Ruby client libraries that provide
access to Google services via their HTTP REST API endpoints. These libraries are
generated and updated automatically based on the discovery documents published
by the service, and they handle most concerns such as authentication,
pagination, retry, timeouts, and logging. You can use this client to access the
Managed Service for Microsoft Active Directory API, but note that some services
may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-managedidentities-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-managedidentities_v1.


%package       -n gem-google-apis-manufacturers-v1
Version:       0.16.0
Release:       alt1.1
Summary:       Simple REST client for Manufacturer Center API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-manufacturers_v1) = 0.16.0

%description   -n gem-google-apis-manufacturers-v1
This is the simple REST client for Manufacturer Center API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Manufacturer Center API, but
note that some services may provide a separate modern client that is easier to
use.


%package       -n gem-google-apis-manufacturers-v1-doc
Version:       0.16.0
Release:       alt1.1
Summary:       Simple REST client for Manufacturer Center API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-manufacturers_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-manufacturers_v1) = 0.16.0

%description   -n gem-google-apis-manufacturers-v1-doc
Simple REST client for Manufacturer Center API V1 documentation files.

This is the simple REST client for Manufacturer Center API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Manufacturer Center API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-manufacturers-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-manufacturers_v1.


%package       -n gem-google-apis-manufacturers-v1-devel
Version:       0.16.0
Release:       alt1.1
Summary:       Simple REST client for Manufacturer Center API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-manufacturers_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-manufacturers_v1) = 0.16.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-manufacturers-v1-devel
Simple REST client for Manufacturer Center API V1 development package.

This is the simple REST client for Manufacturer Center API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Manufacturer Center API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-manufacturers-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-manufacturers_v1.


%package       -n gem-google-apis-memcache-v1
Version:       0.25.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Memorystore for Memcached API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-memcache_v1) = 0.25.0

%description   -n gem-google-apis-memcache-v1
This is the simple REST client for Cloud Memorystore for Memcached API V1.
Simple REST clients are Ruby client libraries that provide access to Google
services via their HTTP REST API endpoints. These libraries are generated and
updated automatically based on the discovery documents published by the service,
and they handle most concerns such as authentication, pagination, retry,
timeouts, and logging. You can use this client to access the Cloud Memorystore
for Memcached API, but note that some services may provide a separate modern
client that is easier to use.


%package       -n gem-google-apis-memcache-v1-doc
Version:       0.25.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Memorystore for Memcached API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-memcache_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-memcache_v1) = 0.25.0

%description   -n gem-google-apis-memcache-v1-doc
Simple REST client for Cloud Memorystore for Memcached API V1 documentation
files.

This is the simple REST client for Cloud Memorystore for Memcached API V1.
Simple REST clients are Ruby client libraries that provide access to Google
services via their HTTP REST API endpoints. These libraries are generated and
updated automatically based on the discovery documents published by the service,
and they handle most concerns such as authentication, pagination, retry,
timeouts, and logging. You can use this client to access the Cloud Memorystore
for Memcached API, but note that some services may provide a separate modern
client that is easier to use.

%description   -n gem-google-apis-memcache-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-memcache_v1.


%package       -n gem-google-apis-memcache-v1-devel
Version:       0.25.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Memorystore for Memcached API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-memcache_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-memcache_v1) = 0.25.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-memcache-v1-devel
Simple REST client for Cloud Memorystore for Memcached API V1 development
package.

This is the simple REST client for Cloud Memorystore for Memcached API V1.
Simple REST clients are Ruby client libraries that provide access to Google
services via their HTTP REST API endpoints. These libraries are generated and
updated automatically based on the discovery documents published by the service,
and they handle most concerns such as authentication, pagination, retry,
timeouts, and logging. You can use this client to access the Cloud Memorystore
for Memcached API, but note that some services may provide a separate modern
client that is easier to use.

%description   -n gem-google-apis-memcache-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-memcache_v1.


%package       -n gem-google-apis-metastore-v1beta
Version:       0.37.0
Release:       alt1.1
Summary:       Simple REST client for Dataproc Metastore API V1beta
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-metastore_v1beta) = 0.37.0

%description   -n gem-google-apis-metastore-v1beta
This is the simple REST client for Dataproc Metastore API V1beta. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Dataproc Metastore API, but
note that some services may provide a separate modern client that is easier to
use.


%package       -n gem-google-apis-metastore-v1beta-doc
Version:       0.37.0
Release:       alt1.1
Summary:       Simple REST client for Dataproc Metastore API V1beta documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-metastore_v1beta
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-metastore_v1beta) = 0.37.0

%description   -n gem-google-apis-metastore-v1beta-doc
Simple REST client for Dataproc Metastore API V1beta documentation files.

This is the simple REST client for Dataproc Metastore API V1beta. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Dataproc Metastore API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-metastore-v1beta-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-metastore_v1beta.


%package       -n gem-google-apis-metastore-v1beta-devel
Version:       0.37.0
Release:       alt1.1
Summary:       Simple REST client for Dataproc Metastore API V1beta development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-metastore_v1beta
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-metastore_v1beta) = 0.37.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-metastore-v1beta-devel
Simple REST client for Dataproc Metastore API V1beta development package.

This is the simple REST client for Dataproc Metastore API V1beta. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Dataproc Metastore API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-metastore-v1beta-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-metastore_v1beta.


%package       -n gem-google-apis-ml-v1
Version:       0.28.0
Release:       alt1.1
Summary:       Simple REST client for AI Platform Training & Prediction API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-ml_v1) = 0.28.0

%description   -n gem-google-apis-ml-v1
This is the simple REST client for AI Platform Training & Prediction API V1.
Simple REST clients are Ruby client libraries that provide access to Google
services via their HTTP REST API endpoints. These libraries are generated and
updated automatically based on the discovery documents published by the service,
and they handle most concerns such as authentication, pagination, retry,
timeouts, and logging. You can use this client to access the AI Platform
Training & Prediction API, but note that some services may provide a separate
modern client that is easier to use.


%package       -n gem-google-apis-ml-v1-doc
Version:       0.28.0
Release:       alt1.1
Summary:       Simple REST client for AI Platform Training & Prediction API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-ml_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-ml_v1) = 0.28.0

%description   -n gem-google-apis-ml-v1-doc
Simple REST client for AI Platform Training & Prediction API V1 documentation
files.

This is the simple REST client for AI Platform Training & Prediction API V1.
Simple REST clients are Ruby client libraries that provide access to Google
services via their HTTP REST API endpoints. These libraries are generated and
updated automatically based on the discovery documents published by the service,
and they handle most concerns such as authentication, pagination, retry,
timeouts, and logging. You can use this client to access the AI Platform
Training & Prediction API, but note that some services may provide a separate
modern client that is easier to use.

%description   -n gem-google-apis-ml-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-ml_v1.


%package       -n gem-google-apis-ml-v1-devel
Version:       0.28.0
Release:       alt1.1
Summary:       Simple REST client for AI Platform Training & Prediction API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-ml_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-ml_v1) = 0.28.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-ml-v1-devel
Simple REST client for AI Platform Training & Prediction API V1 development
package.

This is the simple REST client for AI Platform Training & Prediction API V1.
Simple REST clients are Ruby client libraries that provide access to Google
services via their HTTP REST API endpoints. These libraries are generated and
updated automatically based on the discovery documents published by the service,
and they handle most concerns such as authentication, pagination, retry,
timeouts, and logging. You can use this client to access the AI Platform
Training & Prediction API, but note that some services may provide a separate
modern client that is easier to use.

%description   -n gem-google-apis-ml-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-ml_v1.


%package       -n gem-google-apis-monitoring-v1
Version:       0.29.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Monitoring API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-monitoring_v1) = 0.29.0

%description   -n gem-google-apis-monitoring-v1
This is the simple REST client for Cloud Monitoring API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Cloud Monitoring API, but note that some
services may provide a separate modern client that is easier to use.


%package       -n gem-google-apis-monitoring-v1-doc
Version:       0.29.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Monitoring API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-monitoring_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-monitoring_v1) = 0.29.0

%description   -n gem-google-apis-monitoring-v1-doc
Simple REST client for Cloud Monitoring API V1 documentation files.

This is the simple REST client for Cloud Monitoring API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Cloud Monitoring API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-monitoring-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-monitoring_v1.


%package       -n gem-google-apis-monitoring-v1-devel
Version:       0.29.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Monitoring API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-monitoring_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-monitoring_v1) = 0.29.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-monitoring-v1-devel
Simple REST client for Cloud Monitoring API V1 development package.

This is the simple REST client for Cloud Monitoring API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Cloud Monitoring API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-monitoring-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-monitoring_v1.


%package       -n gem-google-apis-monitoring-v3
Version:       0.36.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Monitoring API V3
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-monitoring_v3) = 0.36.0

%description   -n gem-google-apis-monitoring-v3
This is the simple REST client for Cloud Monitoring API V3. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Cloud Monitoring API, but note that some
services may provide a separate modern client that is easier to use.


%package       -n gem-google-apis-monitoring-v3-doc
Version:       0.36.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Monitoring API V3 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-monitoring_v3
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-monitoring_v3) = 0.36.0

%description   -n gem-google-apis-monitoring-v3-doc
Simple REST client for Cloud Monitoring API V3 documentation files.

This is the simple REST client for Cloud Monitoring API V3. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Cloud Monitoring API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-monitoring-v3-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-monitoring_v3.


%package       -n gem-google-apis-monitoring-v3-devel
Version:       0.36.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Monitoring API V3 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-monitoring_v3
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-monitoring_v3) = 0.36.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-monitoring-v3-devel
Simple REST client for Cloud Monitoring API V3 development package.

This is the simple REST client for Cloud Monitoring API V3. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Cloud Monitoring API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-monitoring-v3-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-monitoring_v3.


%package       -n gem-google-apis-mybusinessaccountmanagement-v1
Version:       0.18.0
Release:       alt1.1
Summary:       Simple REST client for My Business Account Management API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-mybusinessaccountmanagement_v1) = 0.18.0

%description   -n gem-google-apis-mybusinessaccountmanagement-v1
This is the simple REST client for My Business Account Management API V1. Simple
REST clients are Ruby client libraries that provide access to Google services
via their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the My Business Account
Management API, but note that some services may provide a separate modern client
that is easier to use.


%package       -n gem-google-apis-mybusinessaccountmanagement-v1-doc
Version:       0.18.0
Release:       alt1.1
Summary:       Simple REST client for My Business Account Management API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-mybusinessaccountmanagement_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-mybusinessaccountmanagement_v1) = 0.18.0

%description   -n gem-google-apis-mybusinessaccountmanagement-v1-doc
Simple REST client for My Business Account Management API V1 documentation
files.

This is the simple REST client for My Business Account Management API V1. Simple
REST clients are Ruby client libraries that provide access to Google services
via their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the My Business Account
Management API, but note that some services may provide a separate modern client
that is easier to use.

%description   -n gem-google-apis-mybusinessaccountmanagement-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-mybusinessaccountmanagement_v1.


%package       -n gem-google-apis-mybusinessaccountmanagement-v1-devel
Version:       0.18.0
Release:       alt1.1
Summary:       Simple REST client for My Business Account Management API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-mybusinessaccountmanagement_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-mybusinessaccountmanagement_v1) = 0.18.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-mybusinessaccountmanagement-v1-devel
Simple REST client for My Business Account Management API V1 development
package.

This is the simple REST client for My Business Account Management API V1. Simple
REST clients are Ruby client libraries that provide access to Google services
via their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the My Business Account
Management API, but note that some services may provide a separate modern client
that is easier to use.

%description   -n gem-google-apis-mybusinessaccountmanagement-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-mybusinessaccountmanagement_v1.


%package       -n gem-google-apis-mybusinessbusinesscalls-v1
Version:       0.6.0
Release:       alt1.1
Summary:       Simple REST client for My Business Business Calls API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-mybusinessbusinesscalls_v1) = 0.6.0

%description   -n gem-google-apis-mybusinessbusinesscalls-v1
This is the simple REST client for My Business Business Calls API V1. Simple
REST clients are Ruby client libraries that provide access to Google services
via their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the My Business Business Calls
API, but note that some services may provide a separate modern client that is
easier to use.


%package       -n gem-google-apis-mybusinessbusinesscalls-v1-doc
Version:       0.6.0
Release:       alt1.1
Summary:       Simple REST client for My Business Business Calls API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-mybusinessbusinesscalls_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-mybusinessbusinesscalls_v1) = 0.6.0

%description   -n gem-google-apis-mybusinessbusinesscalls-v1-doc
Simple REST client for My Business Business Calls API V1 documentation
files.

This is the simple REST client for My Business Business Calls API V1. Simple
REST clients are Ruby client libraries that provide access to Google services
via their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the My Business Business Calls
API, but note that some services may provide a separate modern client that is
easier to use.

%description   -n gem-google-apis-mybusinessbusinesscalls-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-mybusinessbusinesscalls_v1.


%package       -n gem-google-apis-mybusinessbusinesscalls-v1-devel
Version:       0.6.0
Release:       alt1.1
Summary:       Simple REST client for My Business Business Calls API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-mybusinessbusinesscalls_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-mybusinessbusinesscalls_v1) = 0.6.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-mybusinessbusinesscalls-v1-devel
Simple REST client for My Business Business Calls API V1 development
package.

This is the simple REST client for My Business Business Calls API V1. Simple
REST clients are Ruby client libraries that provide access to Google services
via their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the My Business Business Calls
API, but note that some services may provide a separate modern client that is
easier to use.

%description   -n gem-google-apis-mybusinessbusinesscalls-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-mybusinessbusinesscalls_v1.


%package       -n gem-google-apis-mybusinessbusinessinformation-v1
Version:       0.13.0
Release:       alt1.1
Summary:       Simple REST client for My Business Business Information API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-mybusinessbusinessinformation_v1) = 0.13.0

%description   -n gem-google-apis-mybusinessbusinessinformation-v1
This is the simple REST client for My Business Business Information API V1.
Simple REST clients are Ruby client libraries that provide access to Google
services via their HTTP REST API endpoints. These libraries are generated and
updated automatically based on the discovery documents published by the service,
and they handle most concerns such as authentication, pagination, retry,
timeouts, and logging. You can use this client to access the My Business
Business Information API, but note that some services may provide a separate
modern client that is easier to use.


%package       -n gem-google-apis-mybusinessbusinessinformation-v1-doc
Version:       0.13.0
Release:       alt1.1
Summary:       Simple REST client for My Business Business Information API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-mybusinessbusinessinformation_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-mybusinessbusinessinformation_v1) = 0.13.0

%description   -n gem-google-apis-mybusinessbusinessinformation-v1-doc
Simple REST client for My Business Business Information API V1 documentation
files.

This is the simple REST client for My Business Business Information API V1.
Simple REST clients are Ruby client libraries that provide access to Google
services via their HTTP REST API endpoints. These libraries are generated and
updated automatically based on the discovery documents published by the service,
and they handle most concerns such as authentication, pagination, retry,
timeouts, and logging. You can use this client to access the My Business
Business Information API, but note that some services may provide a separate
modern client that is easier to use.

%description   -n gem-google-apis-mybusinessbusinessinformation-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-mybusinessbusinessinformation_v1.


%package       -n gem-google-apis-mybusinessbusinessinformation-v1-devel
Version:       0.13.0
Release:       alt1.1
Summary:       Simple REST client for My Business Business Information API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-mybusinessbusinessinformation_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-mybusinessbusinessinformation_v1) = 0.13.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-mybusinessbusinessinformation-v1-devel
Simple REST client for My Business Business Information API V1 development
package.

This is the simple REST client for My Business Business Information API V1.
Simple REST clients are Ruby client libraries that provide access to Google
services via their HTTP REST API endpoints. These libraries are generated and
updated automatically based on the discovery documents published by the service,
and they handle most concerns such as authentication, pagination, retry,
timeouts, and logging. You can use this client to access the My Business
Business Information API, but note that some services may provide a separate
modern client that is easier to use.

%description   -n gem-google-apis-mybusinessbusinessinformation-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-mybusinessbusinessinformation_v1.


%package       -n gem-google-apis-mybusinesslodging-v1
Version:       0.12.0
Release:       alt1.1
Summary:       Simple REST client for My Business Lodging API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-mybusinesslodging_v1) = 0.12.0

%description   -n gem-google-apis-mybusinesslodging-v1
This is the simple REST client for My Business Lodging API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the My Business Lodging API, but
note that some services may provide a separate modern client that is easier to
use.


%package       -n gem-google-apis-mybusinesslodging-v1-doc
Version:       0.12.0
Release:       alt1.1
Summary:       Simple REST client for My Business Lodging API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-mybusinesslodging_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-mybusinesslodging_v1) = 0.12.0

%description   -n gem-google-apis-mybusinesslodging-v1-doc
Simple REST client for My Business Lodging API V1 documentation files.

This is the simple REST client for My Business Lodging API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the My Business Lodging API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-mybusinesslodging-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-mybusinesslodging_v1.


%package       -n gem-google-apis-mybusinesslodging-v1-devel
Version:       0.12.0
Release:       alt1.1
Summary:       Simple REST client for My Business Lodging API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-mybusinesslodging_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-mybusinesslodging_v1) = 0.12.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-mybusinesslodging-v1-devel
Simple REST client for My Business Lodging API V1 development package.

This is the simple REST client for My Business Lodging API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the My Business Lodging API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-mybusinesslodging-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-mybusinesslodging_v1.


%package       -n gem-google-apis-mybusinessnotifications-v1
Version:       0.8.0
Release:       alt1.1
Summary:       Simple REST client for My Business Notifications API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-mybusinessnotifications_v1) = 0.8.0

%description   -n gem-google-apis-mybusinessnotifications-v1
This is the simple REST client for My Business Notifications API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the My Business Notifications
API, but note that some services may provide a separate modern client that is
easier to use.


%package       -n gem-google-apis-mybusinessnotifications-v1-doc
Version:       0.8.0
Release:       alt1.1
Summary:       Simple REST client for My Business Notifications API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-mybusinessnotifications_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-mybusinessnotifications_v1) = 0.8.0

%description   -n gem-google-apis-mybusinessnotifications-v1-doc
Simple REST client for My Business Notifications API V1 documentation
files.

This is the simple REST client for My Business Notifications API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the My Business Notifications
API, but note that some services may provide a separate modern client that is
easier to use.

%description   -n gem-google-apis-mybusinessnotifications-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-mybusinessnotifications_v1.


%package       -n gem-google-apis-mybusinessnotifications-v1-devel
Version:       0.8.0
Release:       alt1.1
Summary:       Simple REST client for My Business Notifications API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-mybusinessnotifications_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-mybusinessnotifications_v1) = 0.8.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-mybusinessnotifications-v1-devel
Simple REST client for My Business Notifications API V1 development
package.

This is the simple REST client for My Business Notifications API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the My Business Notifications
API, but note that some services may provide a separate modern client that is
easier to use.

%description   -n gem-google-apis-mybusinessnotifications-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-mybusinessnotifications_v1.


%package       -n gem-google-apis-mybusinessplaceactions-v1
Version:       0.13.0
Release:       alt1.1
Summary:       Simple REST client for My Business Place Actions API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-mybusinessplaceactions_v1) = 0.13.0

%description   -n gem-google-apis-mybusinessplaceactions-v1
This is the simple REST client for My Business Place Actions API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the My Business Place Actions
API, but note that some services may provide a separate modern client that is
easier to use.


%package       -n gem-google-apis-mybusinessplaceactions-v1-doc
Version:       0.13.0
Release:       alt1.1
Summary:       Simple REST client for My Business Place Actions API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-mybusinessplaceactions_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-mybusinessplaceactions_v1) = 0.13.0

%description   -n gem-google-apis-mybusinessplaceactions-v1-doc
Simple REST client for My Business Place Actions API V1 documentation
files.

This is the simple REST client for My Business Place Actions API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the My Business Place Actions
API, but note that some services may provide a separate modern client that is
easier to use.

%description   -n gem-google-apis-mybusinessplaceactions-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-mybusinessplaceactions_v1.


%package       -n gem-google-apis-mybusinessplaceactions-v1-devel
Version:       0.13.0
Release:       alt1.1
Summary:       Simple REST client for My Business Place Actions API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-mybusinessplaceactions_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-mybusinessplaceactions_v1) = 0.13.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-mybusinessplaceactions-v1-devel
Simple REST client for My Business Place Actions API V1 development
package.

This is the simple REST client for My Business Place Actions API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the My Business Place Actions
API, but note that some services may provide a separate modern client that is
easier to use.

%description   -n gem-google-apis-mybusinessplaceactions-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-mybusinessplaceactions_v1.


%package       -n gem-google-apis-mybusinessqanda-v1
Version:       0.7.0
Release:       alt1.1
Summary:       Simple REST client for My Business Q&A API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-mybusinessqanda_v1) = 0.7.0

%description   -n gem-google-apis-mybusinessqanda-v1
This is the simple REST client for My Business Q&A API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the My Business Q&A API, but note that some
services may provide a separate modern client that is easier to use.


%package       -n gem-google-apis-mybusinessqanda-v1-doc
Version:       0.7.0
Release:       alt1.1
Summary:       Simple REST client for My Business Q&A API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-mybusinessqanda_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-mybusinessqanda_v1) = 0.7.0

%description   -n gem-google-apis-mybusinessqanda-v1-doc
Simple REST client for My Business Q&A API V1 documentation files.

This is the simple REST client for My Business Q&A API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the My Business Q&A API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-mybusinessqanda-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-mybusinessqanda_v1.


%package       -n gem-google-apis-mybusinessqanda-v1-devel
Version:       0.7.0
Release:       alt1.1
Summary:       Simple REST client for My Business Q&A API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-mybusinessqanda_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-mybusinessqanda_v1) = 0.7.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-mybusinessqanda-v1-devel
Simple REST client for My Business Q&A API V1 development package.

This is the simple REST client for My Business Q&A API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the My Business Q&A API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-mybusinessqanda-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-mybusinessqanda_v1.


%package       -n gem-google-apis-mybusinessverifications-v1
Version:       0.10.0
Release:       alt1.1
Summary:       Simple REST client for My Business Verifications API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-mybusinessverifications_v1) = 0.10.0

%description   -n gem-google-apis-mybusinessverifications-v1
This is the simple REST client for My Business Verifications API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the My Business Verifications
API, but note that some services may provide a separate modern client that is
easier to use.


%package       -n gem-google-apis-mybusinessverifications-v1-doc
Version:       0.10.0
Release:       alt1.1
Summary:       Simple REST client for My Business Verifications API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-mybusinessverifications_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-mybusinessverifications_v1) = 0.10.0

%description   -n gem-google-apis-mybusinessverifications-v1-doc
Simple REST client for My Business Verifications API V1 documentation
files.

This is the simple REST client for My Business Verifications API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the My Business Verifications
API, but note that some services may provide a separate modern client that is
easier to use.

%description   -n gem-google-apis-mybusinessverifications-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-mybusinessverifications_v1.


%package       -n gem-google-apis-mybusinessverifications-v1-devel
Version:       0.10.0
Release:       alt1.1
Summary:       Simple REST client for My Business Verifications API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-mybusinessverifications_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-mybusinessverifications_v1) = 0.10.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-mybusinessverifications-v1-devel
Simple REST client for My Business Verifications API V1 development
package.

This is the simple REST client for My Business Verifications API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the My Business Verifications
API, but note that some services may provide a separate modern client that is
easier to use.

%description   -n gem-google-apis-mybusinessverifications-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-mybusinessverifications_v1.


%package       -n gem-google-apis-pagespeedonline-v5
Version:       0.13.0
Release:       alt1.1
Summary:       Simple REST client for PageSpeed Insights API V5
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-pagespeedonline_v5) = 0.13.0

%description   -n gem-google-apis-pagespeedonline-v5
This is the simple REST client for PageSpeed Insights API V5. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the PageSpeed Insights API, but
note that some services may provide a separate modern client that is easier to
use.


%package       -n gem-google-apis-pagespeedonline-v5-doc
Version:       0.13.0
Release:       alt1.1
Summary:       Simple REST client for PageSpeed Insights API V5 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-pagespeedonline_v5
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-pagespeedonline_v5) = 0.13.0

%description   -n gem-google-apis-pagespeedonline-v5-doc
Simple REST client for PageSpeed Insights API V5 documentation files.

This is the simple REST client for PageSpeed Insights API V5. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the PageSpeed Insights API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-pagespeedonline-v5-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-pagespeedonline_v5.


%package       -n gem-google-apis-pagespeedonline-v5-devel
Version:       0.13.0
Release:       alt1.1
Summary:       Simple REST client for PageSpeed Insights API V5 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-pagespeedonline_v5
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-pagespeedonline_v5) = 0.13.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-pagespeedonline-v5-devel
Simple REST client for PageSpeed Insights API V5 development package.

This is the simple REST client for PageSpeed Insights API V5. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the PageSpeed Insights API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-pagespeedonline-v5-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-pagespeedonline_v5.


%package       -n gem-google-apis-paymentsresellersubscription-v1
Version:       0.22.0
Release:       alt1.1
Summary:       Simple REST client for Payments Reseller Subscription API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-paymentsresellersubscription_v1) = 0.22.0

%description   -n gem-google-apis-paymentsresellersubscription-v1
This is the simple REST client for Payments Reseller Subscription API V1. Simple
REST clients are Ruby client libraries that provide access to Google services
via their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Payments Reseller
Subscription API, but note that some services may provide a separate modern
client that is easier to use.


%package       -n gem-google-apis-paymentsresellersubscription-v1-doc
Version:       0.22.0
Release:       alt1.1
Summary:       Simple REST client for Payments Reseller Subscription API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-paymentsresellersubscription_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-paymentsresellersubscription_v1) = 0.22.0

%description   -n gem-google-apis-paymentsresellersubscription-v1-doc
Simple REST client for Payments Reseller Subscription API V1 documentation
files.

This is the simple REST client for Payments Reseller Subscription API V1. Simple
REST clients are Ruby client libraries that provide access to Google services
via their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Payments Reseller
Subscription API, but note that some services may provide a separate modern
client that is easier to use.

%description   -n gem-google-apis-paymentsresellersubscription-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-paymentsresellersubscription_v1.


%package       -n gem-google-apis-paymentsresellersubscription-v1-devel
Version:       0.22.0
Release:       alt1.1
Summary:       Simple REST client for Payments Reseller Subscription API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-paymentsresellersubscription_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-paymentsresellersubscription_v1) = 0.22.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-paymentsresellersubscription-v1-devel
Simple REST client for Payments Reseller Subscription API V1 development
package.

This is the simple REST client for Payments Reseller Subscription API V1. Simple
REST clients are Ruby client libraries that provide access to Google services
via their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Payments Reseller
Subscription API, but note that some services may provide a separate modern
client that is easier to use.

%description   -n gem-google-apis-paymentsresellersubscription-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-paymentsresellersubscription_v1.


%package       -n gem-google-apis-people-v1
Version:       0.33.0
Release:       alt1.1
Summary:       Simple REST client for People API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-people_v1) = 0.33.0

%description   -n gem-google-apis-people-v1
This is the simple REST client for People API V1. Simple REST clients are Ruby
client libraries that provide access to Google services via their HTTP REST API
endpoints. These libraries are generated and updated automatically based on the
discovery documents published by the service, and they handle most concerns such
as authentication, pagination, retry, timeouts, and logging. You can use this
client to access the People API, but note that some services may provide a
separate modern client that is easier to use.


%package       -n gem-google-apis-people-v1-doc
Version:       0.33.0
Release:       alt1.1
Summary:       Simple REST client for People API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-people_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-people_v1) = 0.33.0

%description   -n gem-google-apis-people-v1-doc
Simple REST client for People API V1 documentation files.

This is the simple REST client for People API V1. Simple REST clients are Ruby
client libraries that provide access to Google services via their HTTP REST API
endpoints. These libraries are generated and updated automatically based on the
discovery documents published by the service, and they handle most concerns such
as authentication, pagination, retry, timeouts, and logging. You can use this
client to access the People API, but note that some services may provide a
separate modern client that is easier to use.

%description   -n gem-google-apis-people-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-people_v1.


%package       -n gem-google-apis-people-v1-devel
Version:       0.33.0
Release:       alt1.1
Summary:       Simple REST client for People API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-people_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-people_v1) = 0.33.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-people-v1-devel
Simple REST client for People API V1 development package.

This is the simple REST client for People API V1. Simple REST clients are Ruby
client libraries that provide access to Google services via their HTTP REST API
endpoints. These libraries are generated and updated automatically based on the
discovery documents published by the service, and they handle most concerns such
as authentication, pagination, retry, timeouts, and logging. You can use this
client to access the People API, but note that some services may provide a
separate modern client that is easier to use.

%description   -n gem-google-apis-people-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-people_v1.


%package       -n gem-google-apis-playablelocations-v3
Version:       0.6.0
Release:       alt1.1
Summary:       Simple REST client for Playable Locations API V3
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.4 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-playablelocations_v3) = 0.6.0

%description   -n gem-google-apis-playablelocations-v3
This is the simple REST client for Playable Locations API V3. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Playable Locations API, but
note that some services may provide a separate modern client that is easier to
use.


%package       -n gem-google-apis-playablelocations-v3-doc
Version:       0.6.0
Release:       alt1.1
Summary:       Simple REST client for Playable Locations API V3 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-playablelocations_v3
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-playablelocations_v3) = 0.6.0

%description   -n gem-google-apis-playablelocations-v3-doc
Simple REST client for Playable Locations API V3 documentation files.

This is the simple REST client for Playable Locations API V3. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Playable Locations API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-playablelocations-v3-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-playablelocations_v3.


%package       -n gem-google-apis-playablelocations-v3-devel
Version:       0.6.0
Release:       alt1.1
Summary:       Simple REST client for Playable Locations API V3 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-playablelocations_v3
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-playablelocations_v3) = 0.6.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-playablelocations-v3-devel
Simple REST client for Playable Locations API V3 development package.

This is the simple REST client for Playable Locations API V3. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Playable Locations API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-playablelocations-v3-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-playablelocations_v3.


%package       -n gem-google-apis-playcustomapp-v1
Version:       0.11.0
Release:       alt1.1
Summary:       Simple REST client for Google Play Custom App Publishing API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-playcustomapp_v1) = 0.11.0

%description   -n gem-google-apis-playcustomapp-v1
This is the simple REST client for Google Play Custom App Publishing API V1.
Simple REST clients are Ruby client libraries that provide access to Google
services via their HTTP REST API endpoints. These libraries are generated and
updated automatically based on the discovery documents published by the service,
and they handle most concerns such as authentication, pagination, retry,
timeouts, and logging. You can use this client to access the Google Play Custom
App Publishing API, but note that some services may provide a separate modern
client that is easier to use.


%package       -n gem-google-apis-playcustomapp-v1-doc
Version:       0.11.0
Release:       alt1.1
Summary:       Simple REST client for Google Play Custom App Publishing API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-playcustomapp_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-playcustomapp_v1) = 0.11.0

%description   -n gem-google-apis-playcustomapp-v1-doc
Simple REST client for Google Play Custom App Publishing API V1 documentation
files.

This is the simple REST client for Google Play Custom App Publishing API V1.
Simple REST clients are Ruby client libraries that provide access to Google
services via their HTTP REST API endpoints. These libraries are generated and
updated automatically based on the discovery documents published by the service,
and they handle most concerns such as authentication, pagination, retry,
timeouts, and logging. You can use this client to access the Google Play Custom
App Publishing API, but note that some services may provide a separate modern
client that is easier to use.

%description   -n gem-google-apis-playcustomapp-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-playcustomapp_v1.


%package       -n gem-google-apis-playcustomapp-v1-devel
Version:       0.11.0
Release:       alt1.1
Summary:       Simple REST client for Google Play Custom App Publishing API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-playcustomapp_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-playcustomapp_v1) = 0.11.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-playcustomapp-v1-devel
Simple REST client for Google Play Custom App Publishing API V1 development
package.

This is the simple REST client for Google Play Custom App Publishing API V1.
Simple REST clients are Ruby client libraries that provide access to Google
services via their HTTP REST API endpoints. These libraries are generated and
updated automatically based on the discovery documents published by the service,
and they handle most concerns such as authentication, pagination, retry,
timeouts, and logging. You can use this client to access the Google Play Custom
App Publishing API, but note that some services may provide a separate modern
client that is easier to use.

%description   -n gem-google-apis-playcustomapp-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-playcustomapp_v1.


%package       -n gem-google-apis-playintegrity-v1
Version:       0.10.0
Release:       alt1.1
Summary:       Simple REST client for Google Play Integrity API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-playintegrity_v1) = 0.10.0

%description   -n gem-google-apis-playintegrity-v1
This is the simple REST client for Google Play Integrity API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Google Play Integrity API,
but note that some services may provide a separate modern client that is easier
to use.


%package       -n gem-google-apis-playintegrity-v1-doc
Version:       0.10.0
Release:       alt1.1
Summary:       Simple REST client for Google Play Integrity API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-playintegrity_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-playintegrity_v1) = 0.10.0

%description   -n gem-google-apis-playintegrity-v1-doc
Simple REST client for Google Play Integrity API V1 documentation files.

This is the simple REST client for Google Play Integrity API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Google Play Integrity API,
but note that some services may provide a separate modern client that is easier
to use.

%description   -n gem-google-apis-playintegrity-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-playintegrity_v1.


%package       -n gem-google-apis-playintegrity-v1-devel
Version:       0.10.0
Release:       alt1.1
Summary:       Simple REST client for Google Play Integrity API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-playintegrity_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-playintegrity_v1) = 0.10.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-playintegrity-v1-devel
Simple REST client for Google Play Integrity API V1 development package.

This is the simple REST client for Google Play Integrity API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Google Play Integrity API,
but note that some services may provide a separate modern client that is easier
to use.

%description   -n gem-google-apis-playintegrity-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-playintegrity_v1.


%package       -n gem-google-apis-policyanalyzer-v1
Version:       0.9.0
Release:       alt1.1
Summary:       Simple REST client for Policy Analyzer API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-policyanalyzer_v1) = 0.9.0

%description   -n gem-google-apis-policyanalyzer-v1
This is the simple REST client for Policy Analyzer API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Policy Analyzer API, but note that some
services may provide a separate modern client that is easier to use.


%package       -n gem-google-apis-policyanalyzer-v1-doc
Version:       0.9.0
Release:       alt1.1
Summary:       Simple REST client for Policy Analyzer API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-policyanalyzer_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-policyanalyzer_v1) = 0.9.0

%description   -n gem-google-apis-policyanalyzer-v1-doc
Simple REST client for Policy Analyzer API V1 documentation files.

This is the simple REST client for Policy Analyzer API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Policy Analyzer API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-policyanalyzer-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-policyanalyzer_v1.


%package       -n gem-google-apis-policyanalyzer-v1-devel
Version:       0.9.0
Release:       alt1.1
Summary:       Simple REST client for Policy Analyzer API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-policyanalyzer_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-policyanalyzer_v1) = 0.9.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-policyanalyzer-v1-devel
Simple REST client for Policy Analyzer API V1 development package.

This is the simple REST client for Policy Analyzer API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Policy Analyzer API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-policyanalyzer-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-policyanalyzer_v1.


%package       -n gem-google-apis-policysimulator-v1
Version:       0.20.0
Release:       alt1.1
Summary:       Simple REST client for Policy Simulator API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-policysimulator_v1) = 0.20.0

%description   -n gem-google-apis-policysimulator-v1
This is the simple REST client for Policy Simulator API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Policy Simulator API, but note that some
services may provide a separate modern client that is easier to use.


%package       -n gem-google-apis-policysimulator-v1-doc
Version:       0.20.0
Release:       alt1.1
Summary:       Simple REST client for Policy Simulator API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-policysimulator_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-policysimulator_v1) = 0.20.0

%description   -n gem-google-apis-policysimulator-v1-doc
Simple REST client for Policy Simulator API V1 documentation files.

This is the simple REST client for Policy Simulator API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Policy Simulator API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-policysimulator-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-policysimulator_v1.


%package       -n gem-google-apis-policysimulator-v1-devel
Version:       0.20.0
Release:       alt1.1
Summary:       Simple REST client for Policy Simulator API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-policysimulator_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-policysimulator_v1) = 0.20.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-policysimulator-v1-devel
Simple REST client for Policy Simulator API V1 development package.

This is the simple REST client for Policy Simulator API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Policy Simulator API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-policysimulator-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-policysimulator_v1.


%package       -n gem-google-apis-policytroubleshooter-v1
Version:       0.20.0
Release:       alt1.1
Summary:       Simple REST client for Policy Troubleshooter API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-policytroubleshooter_v1) = 0.20.0

%description   -n gem-google-apis-policytroubleshooter-v1
This is the simple REST client for Policy Troubleshooter API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Policy Troubleshooter API,
but note that some services may provide a separate modern client that is easier
to use.


%package       -n gem-google-apis-policytroubleshooter-v1-doc
Version:       0.20.0
Release:       alt1.1
Summary:       Simple REST client for Policy Troubleshooter API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-policytroubleshooter_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-policytroubleshooter_v1) = 0.20.0

%description   -n gem-google-apis-policytroubleshooter-v1-doc
Simple REST client for Policy Troubleshooter API V1 documentation files.

This is the simple REST client for Policy Troubleshooter API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Policy Troubleshooter API,
but note that some services may provide a separate modern client that is easier
to use.

%description   -n gem-google-apis-policytroubleshooter-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-policytroubleshooter_v1.


%package       -n gem-google-apis-policytroubleshooter-v1-devel
Version:       0.20.0
Release:       alt1.1
Summary:       Simple REST client for Policy Troubleshooter API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-policytroubleshooter_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-policytroubleshooter_v1) = 0.20.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-policytroubleshooter-v1-devel
Simple REST client for Policy Troubleshooter API V1 development package.

This is the simple REST client for Policy Troubleshooter API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Policy Troubleshooter API,
but note that some services may provide a separate modern client that is easier
to use.

%description   -n gem-google-apis-policytroubleshooter-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-policytroubleshooter_v1.


%package       -n gem-google-apis-policytroubleshooter-v1beta
Version:       0.20.0
Release:       alt1.1
Summary:       Simple REST client for Policy Troubleshooter API V1beta
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-policytroubleshooter_v1beta) = 0.20.0

%description   -n gem-google-apis-policytroubleshooter-v1beta
This is the simple REST client for Policy Troubleshooter API V1beta. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Policy Troubleshooter API,
but note that some services may provide a separate modern client that is easier
to use.


%package       -n gem-google-apis-policytroubleshooter-v1beta-doc
Version:       0.20.0
Release:       alt1.1
Summary:       Simple REST client for Policy Troubleshooter API V1beta documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-policytroubleshooter_v1beta
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-policytroubleshooter_v1beta) = 0.20.0

%description   -n gem-google-apis-policytroubleshooter-v1beta-doc
Simple REST client for Policy Troubleshooter API V1beta documentation
files.

This is the simple REST client for Policy Troubleshooter API V1beta. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Policy Troubleshooter API,
but note that some services may provide a separate modern client that is easier
to use.

%description   -n gem-google-apis-policytroubleshooter-v1beta-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-policytroubleshooter_v1beta.


%package       -n gem-google-apis-policytroubleshooter-v1beta-devel
Version:       0.20.0
Release:       alt1.1
Summary:       Simple REST client for Policy Troubleshooter API V1beta development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-policytroubleshooter_v1beta
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-policytroubleshooter_v1beta) = 0.20.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-policytroubleshooter-v1beta-devel
Simple REST client for Policy Troubleshooter API V1beta development
package.

This is the simple REST client for Policy Troubleshooter API V1beta. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Policy Troubleshooter API,
but note that some services may provide a separate modern client that is easier
to use.

%description   -n gem-google-apis-policytroubleshooter-v1beta-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-policytroubleshooter_v1beta.


%package       -n gem-google-apis-poly-v1
Version:       0.11.0
Release:       alt1.1
Summary:       Simple REST client for Poly API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-poly_v1) = 0.11.0

%description   -n gem-google-apis-poly-v1
This is the simple REST client for Poly API V1. Simple REST clients are Ruby
client libraries that provide access to Google services via their HTTP REST API
endpoints. These libraries are generated and updated automatically based on the
discovery documents published by the service, and they handle most concerns such
as authentication, pagination, retry, timeouts, and logging. You can use this
client to access the Poly API, but note that some services may provide a
separate modern client that is easier to use.


%package       -n gem-google-apis-poly-v1-doc
Version:       0.11.0
Release:       alt1.1
Summary:       Simple REST client for Poly API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-poly_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-poly_v1) = 0.11.0

%description   -n gem-google-apis-poly-v1-doc
Simple REST client for Poly API V1 documentation files.

This is the simple REST client for Poly API V1. Simple REST clients are Ruby
client libraries that provide access to Google services via their HTTP REST API
endpoints. These libraries are generated and updated automatically based on the
discovery documents published by the service, and they handle most concerns such
as authentication, pagination, retry, timeouts, and logging. You can use this
client to access the Poly API, but note that some services may provide a
separate modern client that is easier to use.

%description   -n gem-google-apis-poly-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-poly_v1.


%package       -n gem-google-apis-poly-v1-devel
Version:       0.11.0
Release:       alt1.1
Summary:       Simple REST client for Poly API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-poly_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-poly_v1) = 0.11.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-poly-v1-devel
Simple REST client for Poly API V1 development package.

This is the simple REST client for Poly API V1. Simple REST clients are Ruby
client libraries that provide access to Google services via their HTTP REST API
endpoints. These libraries are generated and updated automatically based on the
discovery documents published by the service, and they handle most concerns such
as authentication, pagination, retry, timeouts, and logging. You can use this
client to access the Poly API, but note that some services may provide a
separate modern client that is easier to use.

%description   -n gem-google-apis-poly-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-poly_v1.


%package       -n gem-google-apis-privateca-v1
Version:       0.25.0
Release:       alt1.1
Summary:       Simple REST client for Certificate Authority API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-privateca_v1) = 0.25.0

%description   -n gem-google-apis-privateca-v1
This is the simple REST client for Certificate Authority API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Certificate Authority API,
but note that some services may provide a separate modern client that is easier
to use.


%package       -n gem-google-apis-privateca-v1-doc
Version:       0.25.0
Release:       alt1.1
Summary:       Simple REST client for Certificate Authority API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-privateca_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-privateca_v1) = 0.25.0

%description   -n gem-google-apis-privateca-v1-doc
Simple REST client for Certificate Authority API V1 documentation files.

This is the simple REST client for Certificate Authority API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Certificate Authority API,
but note that some services may provide a separate modern client that is easier
to use.

%description   -n gem-google-apis-privateca-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-privateca_v1.


%package       -n gem-google-apis-privateca-v1-devel
Version:       0.25.0
Release:       alt1.1
Summary:       Simple REST client for Certificate Authority API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-privateca_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-privateca_v1) = 0.25.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-privateca-v1-devel
Simple REST client for Certificate Authority API V1 development package.

This is the simple REST client for Certificate Authority API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Certificate Authority API,
but note that some services may provide a separate modern client that is easier
to use.

%description   -n gem-google-apis-privateca-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-privateca_v1.


%package       -n gem-google-apis-pubsub-v1
Version:       0.29.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Pub/Sub API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-pubsub_v1) = 0.29.0

%description   -n gem-google-apis-pubsub-v1
This is the simple REST client for Cloud Pub/Sub API V1. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Cloud Pub/Sub API, but note that some services may
provide a separate modern client that is easier to use.


%package       -n gem-google-apis-pubsub-v1-doc
Version:       0.29.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Pub/Sub API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-pubsub_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-pubsub_v1) = 0.29.0

%description   -n gem-google-apis-pubsub-v1-doc
Simple REST client for Cloud Pub/Sub API V1 documentation files.

This is the simple REST client for Cloud Pub/Sub API V1. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Cloud Pub/Sub API, but note that some services may
provide a separate modern client that is easier to use.

%description   -n gem-google-apis-pubsub-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-pubsub_v1.


%package       -n gem-google-apis-pubsub-v1-devel
Version:       0.29.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Pub/Sub API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-pubsub_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-pubsub_v1) = 0.29.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-pubsub-v1-devel
Simple REST client for Cloud Pub/Sub API V1 development package.

This is the simple REST client for Cloud Pub/Sub API V1. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Cloud Pub/Sub API, but note that some services may
provide a separate modern client that is easier to use.

%description   -n gem-google-apis-pubsub-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-pubsub_v1.


%package       -n gem-google-apis-pubsublite-v1
Version:       0.19.0
Release:       alt1.1
Summary:       Simple REST client for Pub/Sub Lite API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-pubsublite_v1) = 0.19.0

%description   -n gem-google-apis-pubsublite-v1
This is the simple REST client for Pub/Sub Lite API V1. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Pub/Sub Lite API, but note that some services may
provide a separate modern client that is easier to use.


%package       -n gem-google-apis-pubsublite-v1-doc
Version:       0.19.0
Release:       alt1.1
Summary:       Simple REST client for Pub/Sub Lite API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-pubsublite_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-pubsublite_v1) = 0.19.0

%description   -n gem-google-apis-pubsublite-v1-doc
Simple REST client for Pub/Sub Lite API V1 documentation files.

This is the simple REST client for Pub/Sub Lite API V1. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Pub/Sub Lite API, but note that some services may
provide a separate modern client that is easier to use.

%description   -n gem-google-apis-pubsublite-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-pubsublite_v1.


%package       -n gem-google-apis-pubsublite-v1-devel
Version:       0.19.0
Release:       alt1.1
Summary:       Simple REST client for Pub/Sub Lite API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-pubsublite_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-pubsublite_v1) = 0.19.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-pubsublite-v1-devel
Simple REST client for Pub/Sub Lite API V1 development package.

This is the simple REST client for Pub/Sub Lite API V1. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Pub/Sub Lite API, but note that some services may
provide a separate modern client that is easier to use.

%description   -n gem-google-apis-pubsublite-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-pubsublite_v1.


%package       -n gem-google-apis-safebrowsing-v4
Version:       0.14.0
Release:       alt1.1
Summary:       Simple REST client for Safe Browsing API V4
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-safebrowsing_v4) = 0.14.0

%description   -n gem-google-apis-safebrowsing-v4
This is the simple REST client for Safe Browsing API V4. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Safe Browsing API, but note that some services may
provide a separate modern client that is easier to use.


%package       -n gem-google-apis-safebrowsing-v4-doc
Version:       0.14.0
Release:       alt1.1
Summary:       Simple REST client for Safe Browsing API V4 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-safebrowsing_v4
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-safebrowsing_v4) = 0.14.0

%description   -n gem-google-apis-safebrowsing-v4-doc
Simple REST client for Safe Browsing API V4 documentation files.

This is the simple REST client for Safe Browsing API V4. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Safe Browsing API, but note that some services may
provide a separate modern client that is easier to use.

%description   -n gem-google-apis-safebrowsing-v4-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-safebrowsing_v4.


%package       -n gem-google-apis-safebrowsing-v4-devel
Version:       0.14.0
Release:       alt1.1
Summary:       Simple REST client for Safe Browsing API V4 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-safebrowsing_v4
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-safebrowsing_v4) = 0.14.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-safebrowsing-v4-devel
Simple REST client for Safe Browsing API V4 development package.

This is the simple REST client for Safe Browsing API V4. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Safe Browsing API, but note that some services may
provide a separate modern client that is easier to use.

%description   -n gem-google-apis-safebrowsing-v4-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-safebrowsing_v4.


%package       -n gem-google-apis-script-v1
Version:       0.17.0
Release:       alt1.1
Summary:       Simple REST client for Apps Script API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-script_v1) = 0.17.0

%description   -n gem-google-apis-script-v1
This is the simple REST client for Apps Script API V1. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Apps Script API, but note that some services may
provide a separate modern client that is easier to use.


%package       -n gem-google-apis-script-v1-doc
Version:       0.17.0
Release:       alt1.1
Summary:       Simple REST client for Apps Script API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-script_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-script_v1) = 0.17.0

%description   -n gem-google-apis-script-v1-doc
Simple REST client for Apps Script API V1 documentation files.

This is the simple REST client for Apps Script API V1. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Apps Script API, but note that some services may
provide a separate modern client that is easier to use.

%description   -n gem-google-apis-script-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-script_v1.


%package       -n gem-google-apis-script-v1-devel
Version:       0.17.0
Release:       alt1.1
Summary:       Simple REST client for Apps Script API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-script_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-script_v1) = 0.17.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-script-v1-devel
Simple REST client for Apps Script API V1 development package.

This is the simple REST client for Apps Script API V1. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Apps Script API, but note that some services may
provide a separate modern client that is easier to use.

%description   -n gem-google-apis-script-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-script_v1.


%package       -n gem-google-apis-searchconsole-v1
Version:       0.13.0
Release:       alt1.1
Summary:       Simple REST client for Google Search Console API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-searchconsole_v1) = 0.13.0

%description   -n gem-google-apis-searchconsole-v1
This is the simple REST client for Google Search Console API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Google Search Console API,
but note that some services may provide a separate modern client that is easier
to use.


%package       -n gem-google-apis-searchconsole-v1-doc
Version:       0.13.0
Release:       alt1.1
Summary:       Simple REST client for Google Search Console API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-searchconsole_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-searchconsole_v1) = 0.13.0

%description   -n gem-google-apis-searchconsole-v1-doc
Simple REST client for Google Search Console API V1 documentation files.

This is the simple REST client for Google Search Console API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Google Search Console API,
but note that some services may provide a separate modern client that is easier
to use.

%description   -n gem-google-apis-searchconsole-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-searchconsole_v1.


%package       -n gem-google-apis-searchconsole-v1-devel
Version:       0.13.0
Release:       alt1.1
Summary:       Simple REST client for Google Search Console API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-searchconsole_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-searchconsole_v1) = 0.13.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-searchconsole-v1-devel
Simple REST client for Google Search Console API V1 development package.

This is the simple REST client for Google Search Console API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Google Search Console API,
but note that some services may provide a separate modern client that is easier
to use.

%description   -n gem-google-apis-searchconsole-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-searchconsole_v1.


%package       -n gem-google-apis-secretmanager-v1
Version:       0.30.0
Release:       alt1.1
Summary:       Simple REST client for Secret Manager API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-secretmanager_v1) = 0.30.0

%description   -n gem-google-apis-secretmanager-v1
This is the simple REST client for Secret Manager API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Secret Manager API, but note that some
services may provide a separate modern client that is easier to use.


%package       -n gem-google-apis-secretmanager-v1-doc
Version:       0.30.0
Release:       alt1.1
Summary:       Simple REST client for Secret Manager API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-secretmanager_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-secretmanager_v1) = 0.30.0

%description   -n gem-google-apis-secretmanager-v1-doc
Simple REST client for Secret Manager API V1 documentation files.

This is the simple REST client for Secret Manager API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Secret Manager API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-secretmanager-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-secretmanager_v1.


%package       -n gem-google-apis-secretmanager-v1-devel
Version:       0.30.0
Release:       alt1.1
Summary:       Simple REST client for Secret Manager API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-secretmanager_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-secretmanager_v1) = 0.30.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-secretmanager-v1-devel
Simple REST client for Secret Manager API V1 development package.

This is the simple REST client for Secret Manager API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Secret Manager API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-secretmanager-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-secretmanager_v1.


%package       -n gem-google-apis-securitycenter-v1
Version:       0.44.0
Release:       alt1.1
Summary:       Simple REST client for Security Command Center API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-securitycenter_v1) = 0.44.0

%description   -n gem-google-apis-securitycenter-v1
This is the simple REST client for Security Command Center API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Security Command Center API,
but note that some services may provide a separate modern client that is easier
to use.


%package       -n gem-google-apis-securitycenter-v1-doc
Version:       0.44.0
Release:       alt1.1
Summary:       Simple REST client for Security Command Center API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-securitycenter_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-securitycenter_v1) = 0.44.0

%description   -n gem-google-apis-securitycenter-v1-doc
Simple REST client for Security Command Center API V1 documentation files.

This is the simple REST client for Security Command Center API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Security Command Center API,
but note that some services may provide a separate modern client that is easier
to use.

%description   -n gem-google-apis-securitycenter-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-securitycenter_v1.


%package       -n gem-google-apis-securitycenter-v1-devel
Version:       0.44.0
Release:       alt1.1
Summary:       Simple REST client for Security Command Center API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-securitycenter_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-securitycenter_v1) = 0.44.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-securitycenter-v1-devel
Simple REST client for Security Command Center API V1 development package.

This is the simple REST client for Security Command Center API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Security Command Center API,
but note that some services may provide a separate modern client that is easier
to use.

%description   -n gem-google-apis-securitycenter-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-securitycenter_v1.


%package       -n gem-google-apis-serviceconsumermanagement-v1
Version:       0.27.0
Release:       alt1.1
Summary:       Simple REST client for Service Consumer Management API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-serviceconsumermanagement_v1) = 0.27.0

%description   -n gem-google-apis-serviceconsumermanagement-v1
This is the simple REST client for Service Consumer Management API V1. Simple
REST clients are Ruby client libraries that provide access to Google services
via their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Service Consumer Management
API, but note that some services may provide a separate modern client that is
easier to use.


%package       -n gem-google-apis-serviceconsumermanagement-v1-doc
Version:       0.27.0
Release:       alt1.1
Summary:       Simple REST client for Service Consumer Management API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-serviceconsumermanagement_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-serviceconsumermanagement_v1) = 0.27.0

%description   -n gem-google-apis-serviceconsumermanagement-v1-doc
Simple REST client for Service Consumer Management API V1 documentation
files.

This is the simple REST client for Service Consumer Management API V1. Simple
REST clients are Ruby client libraries that provide access to Google services
via their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Service Consumer Management
API, but note that some services may provide a separate modern client that is
easier to use.

%description   -n gem-google-apis-serviceconsumermanagement-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-serviceconsumermanagement_v1.


%package       -n gem-google-apis-serviceconsumermanagement-v1-devel
Version:       0.27.0
Release:       alt1.1
Summary:       Simple REST client for Service Consumer Management API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-serviceconsumermanagement_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-serviceconsumermanagement_v1) = 0.27.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-serviceconsumermanagement-v1-devel
Simple REST client for Service Consumer Management API V1 development
package.

This is the simple REST client for Service Consumer Management API V1. Simple
REST clients are Ruby client libraries that provide access to Google services
via their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Service Consumer Management
API, but note that some services may provide a separate modern client that is
easier to use.

%description   -n gem-google-apis-serviceconsumermanagement-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-serviceconsumermanagement_v1.


%package       -n gem-google-apis-servicecontrol-v1
Version:       0.25.0
Release:       alt1.1
Summary:       Simple REST client for Service Control API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-servicecontrol_v1) = 0.25.0

%description   -n gem-google-apis-servicecontrol-v1
This is the simple REST client for Service Control API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Service Control API, but note that some
services may provide a separate modern client that is easier to use.


%package       -n gem-google-apis-servicecontrol-v1-doc
Version:       0.25.0
Release:       alt1.1
Summary:       Simple REST client for Service Control API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-servicecontrol_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-servicecontrol_v1) = 0.25.0

%description   -n gem-google-apis-servicecontrol-v1-doc
Simple REST client for Service Control API V1 documentation files.

This is the simple REST client for Service Control API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Service Control API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-servicecontrol-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-servicecontrol_v1.


%package       -n gem-google-apis-servicecontrol-v1-devel
Version:       0.25.0
Release:       alt1.1
Summary:       Simple REST client for Service Control API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-servicecontrol_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-servicecontrol_v1) = 0.25.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-servicecontrol-v1-devel
Simple REST client for Service Control API V1 development package.

This is the simple REST client for Service Control API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Service Control API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-servicecontrol-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-servicecontrol_v1.


%package       -n gem-google-apis-servicecontrol-v2
Version:       0.24.0
Release:       alt1.1
Summary:       Simple REST client for Service Control API V2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-servicecontrol_v2) = 0.24.0

%description   -n gem-google-apis-servicecontrol-v2
This is the simple REST client for Service Control API V2. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Service Control API, but note that some
services may provide a separate modern client that is easier to use.


%package       -n gem-google-apis-servicecontrol-v2-doc
Version:       0.24.0
Release:       alt1.1
Summary:       Simple REST client for Service Control API V2 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-servicecontrol_v2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-servicecontrol_v2) = 0.24.0

%description   -n gem-google-apis-servicecontrol-v2-doc
Simple REST client for Service Control API V2 documentation files.

This is the simple REST client for Service Control API V2. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Service Control API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-servicecontrol-v2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-servicecontrol_v2.


%package       -n gem-google-apis-servicecontrol-v2-devel
Version:       0.24.0
Release:       alt1.1
Summary:       Simple REST client for Service Control API V2 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-servicecontrol_v2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-servicecontrol_v2) = 0.24.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-servicecontrol-v2-devel
Simple REST client for Service Control API V2 development package.

This is the simple REST client for Service Control API V2. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Service Control API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-servicecontrol-v2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-servicecontrol_v2.


%package       -n gem-google-apis-servicedirectory-v1
Version:       0.24.0
Release:       alt1.1
Summary:       Simple REST client for Service Directory API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-servicedirectory_v1) = 0.24.0

%description   -n gem-google-apis-servicedirectory-v1
This is the simple REST client for Service Directory API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Service Directory API, but note that some
services may provide a separate modern client that is easier to use.


%package       -n gem-google-apis-servicedirectory-v1-doc
Version:       0.24.0
Release:       alt1.1
Summary:       Simple REST client for Service Directory API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-servicedirectory_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-servicedirectory_v1) = 0.24.0

%description   -n gem-google-apis-servicedirectory-v1-doc
Simple REST client for Service Directory API V1 documentation files.

This is the simple REST client for Service Directory API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Service Directory API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-servicedirectory-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-servicedirectory_v1.


%package       -n gem-google-apis-servicedirectory-v1-devel
Version:       0.24.0
Release:       alt1.1
Summary:       Simple REST client for Service Directory API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-servicedirectory_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-servicedirectory_v1) = 0.24.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-servicedirectory-v1-devel
Simple REST client for Service Directory API V1 development package.

This is the simple REST client for Service Directory API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Service Directory API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-servicedirectory-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-servicedirectory_v1.


%package       -n gem-google-apis-servicemanagement-v1
Version:       0.35.0
Release:       alt1.1
Summary:       Simple REST client for Service Management API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-servicemanagement_v1) = 0.35.0

%description   -n gem-google-apis-servicemanagement-v1
This is the simple REST client for Service Management API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Service Management API, but
note that some services may provide a separate modern client that is easier to
use.


%package       -n gem-google-apis-servicemanagement-v1-doc
Version:       0.35.0
Release:       alt1.1
Summary:       Simple REST client for Service Management API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-servicemanagement_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-servicemanagement_v1) = 0.35.0

%description   -n gem-google-apis-servicemanagement-v1-doc
Simple REST client for Service Management API V1 documentation files.

This is the simple REST client for Service Management API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Service Management API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-servicemanagement-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-servicemanagement_v1.


%package       -n gem-google-apis-servicemanagement-v1-devel
Version:       0.35.0
Release:       alt1.1
Summary:       Simple REST client for Service Management API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-servicemanagement_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-servicemanagement_v1) = 0.35.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-servicemanagement-v1-devel
Simple REST client for Service Management API V1 development package.

This is the simple REST client for Service Management API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Service Management API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-servicemanagement-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-servicemanagement_v1.


%package       -n gem-google-apis-servicenetworking-v1
Version:       0.33.0
Release:       alt1.1
Summary:       Simple REST client for Service Networking API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-servicenetworking_v1) = 0.33.0

%description   -n gem-google-apis-servicenetworking-v1
This is the simple REST client for Service Networking API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Service Networking API, but
note that some services may provide a separate modern client that is easier to
use.


%package       -n gem-google-apis-servicenetworking-v1-doc
Version:       0.33.0
Release:       alt1.1
Summary:       Simple REST client for Service Networking API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-servicenetworking_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-servicenetworking_v1) = 0.33.0

%description   -n gem-google-apis-servicenetworking-v1-doc
Simple REST client for Service Networking API V1 documentation files.

This is the simple REST client for Service Networking API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Service Networking API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-servicenetworking-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-servicenetworking_v1.


%package       -n gem-google-apis-servicenetworking-v1-devel
Version:       0.33.0
Release:       alt1.1
Summary:       Simple REST client for Service Networking API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-servicenetworking_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-servicenetworking_v1) = 0.33.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-servicenetworking-v1-devel
Simple REST client for Service Networking API V1 development package.

This is the simple REST client for Service Networking API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Service Networking API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-servicenetworking-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-servicenetworking_v1.


%package       -n gem-google-apis-servicenetworking-v1beta
Version:       0.29.0
Release:       alt1.1
Summary:       Simple REST client for Service Networking API V1beta
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-servicenetworking_v1beta) = 0.29.0

%description   -n gem-google-apis-servicenetworking-v1beta
This is the simple REST client for Service Networking API V1beta. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Service Networking API, but
note that some services may provide a separate modern client that is easier to
use.


%package       -n gem-google-apis-servicenetworking-v1beta-doc
Version:       0.29.0
Release:       alt1.1
Summary:       Simple REST client for Service Networking API V1beta documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-servicenetworking_v1beta
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-servicenetworking_v1beta) = 0.29.0

%description   -n gem-google-apis-servicenetworking-v1beta-doc
Simple REST client for Service Networking API V1beta documentation files.

This is the simple REST client for Service Networking API V1beta. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Service Networking API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-servicenetworking-v1beta-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-servicenetworking_v1beta.


%package       -n gem-google-apis-servicenetworking-v1beta-devel
Version:       0.29.0
Release:       alt1.1
Summary:       Simple REST client for Service Networking API V1beta development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-servicenetworking_v1beta
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-servicenetworking_v1beta) = 0.29.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-servicenetworking-v1beta-devel
Simple REST client for Service Networking API V1beta development package.

This is the simple REST client for Service Networking API V1beta. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Service Networking API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-servicenetworking-v1beta-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-servicenetworking_v1beta.


%package       -n gem-google-apis-serviceusage-v1
Version:       0.26.0
Release:       alt1.1
Summary:       Simple REST client for Service Usage API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-serviceusage_v1) = 0.26.0

%description   -n gem-google-apis-serviceusage-v1
This is the simple REST client for Service Usage API V1. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Service Usage API, but note that some services may
provide a separate modern client that is easier to use.


%package       -n gem-google-apis-serviceusage-v1-doc
Version:       0.26.0
Release:       alt1.1
Summary:       Simple REST client for Service Usage API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-serviceusage_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-serviceusage_v1) = 0.26.0

%description   -n gem-google-apis-serviceusage-v1-doc
Simple REST client for Service Usage API V1 documentation files.

This is the simple REST client for Service Usage API V1. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Service Usage API, but note that some services may
provide a separate modern client that is easier to use.

%description   -n gem-google-apis-serviceusage-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-serviceusage_v1.


%package       -n gem-google-apis-serviceusage-v1-devel
Version:       0.26.0
Release:       alt1.1
Summary:       Simple REST client for Service Usage API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-serviceusage_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-serviceusage_v1) = 0.26.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-serviceusage-v1-devel
Simple REST client for Service Usage API V1 development package.

This is the simple REST client for Service Usage API V1. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Service Usage API, but note that some services may
provide a separate modern client that is easier to use.

%description   -n gem-google-apis-serviceusage-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-serviceusage_v1.


%package       -n gem-google-apis-sheets-v4
Version:       0.19.0
Release:       alt1.1
Summary:       Simple REST client for Google Sheets API V4
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-sheets_v4) = 0.19.0

%description   -n gem-google-apis-sheets-v4
This is the simple REST client for Google Sheets API V4. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Google Sheets API, but note that some services may
provide a separate modern client that is easier to use.


%package       -n gem-google-apis-sheets-v4-doc
Version:       0.19.0
Release:       alt1.1
Summary:       Simple REST client for Google Sheets API V4 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-sheets_v4
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-sheets_v4) = 0.19.0

%description   -n gem-google-apis-sheets-v4-doc
Simple REST client for Google Sheets API V4 documentation files.

This is the simple REST client for Google Sheets API V4. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Google Sheets API, but note that some services may
provide a separate modern client that is easier to use.

%description   -n gem-google-apis-sheets-v4-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-sheets_v4.


%package       -n gem-google-apis-sheets-v4-devel
Version:       0.19.0
Release:       alt1.1
Summary:       Simple REST client for Google Sheets API V4 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-sheets_v4
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-sheets_v4) = 0.19.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-sheets-v4-devel
Simple REST client for Google Sheets API V4 development package.

This is the simple REST client for Google Sheets API V4. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Google Sheets API, but note that some services may
provide a separate modern client that is easier to use.

%description   -n gem-google-apis-sheets-v4-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-sheets_v4.


%package       -n gem-google-apis-site-verification-v1
Version:       0.11.0
Release:       alt1.1
Summary:       Simple REST client for Google Site Verification API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-site_verification_v1) = 0.11.0

%description   -n gem-google-apis-site-verification-v1
This is the simple REST client for Google Site Verification API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Google Site Verification API,
but note that some services may provide a separate modern client that is easier
to use.


%package       -n gem-google-apis-site-verification-v1-doc
Version:       0.11.0
Release:       alt1.1
Summary:       Simple REST client for Google Site Verification API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-site_verification_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-site_verification_v1) = 0.11.0

%description   -n gem-google-apis-site-verification-v1-doc
Simple REST client for Google Site Verification API V1 documentation
files.

This is the simple REST client for Google Site Verification API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Google Site Verification API,
but note that some services may provide a separate modern client that is easier
to use.

%description   -n gem-google-apis-site-verification-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-site_verification_v1.


%package       -n gem-google-apis-site-verification-v1-devel
Version:       0.11.0
Release:       alt1.1
Summary:       Simple REST client for Google Site Verification API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-site_verification_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-site_verification_v1) = 0.11.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-site-verification-v1-devel
Simple REST client for Google Site Verification API V1 development
package.

This is the simple REST client for Google Site Verification API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Google Site Verification API,
but note that some services may provide a separate modern client that is easier
to use.

%description   -n gem-google-apis-site-verification-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-site_verification_v1.


%package       -n gem-google-apis-slides-v1
Version:       0.20.0
Release:       alt1.1
Summary:       Simple REST client for Google Slides API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-slides_v1) = 0.20.0

%description   -n gem-google-apis-slides-v1
This is the simple REST client for Google Slides API V1. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Google Slides API, but note that some services may
provide a separate modern client that is easier to use.


%package       -n gem-google-apis-slides-v1-doc
Version:       0.20.0
Release:       alt1.1
Summary:       Simple REST client for Google Slides API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-slides_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-slides_v1) = 0.20.0

%description   -n gem-google-apis-slides-v1-doc
Simple REST client for Google Slides API V1 documentation files.

This is the simple REST client for Google Slides API V1. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Google Slides API, but note that some services may
provide a separate modern client that is easier to use.

%description   -n gem-google-apis-slides-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-slides_v1.


%package       -n gem-google-apis-slides-v1-devel
Version:       0.20.0
Release:       alt1.1
Summary:       Simple REST client for Google Slides API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-slides_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-slides_v1) = 0.20.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-slides-v1-devel
Simple REST client for Google Slides API V1 development package.

This is the simple REST client for Google Slides API V1. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Google Slides API, but note that some services may
provide a separate modern client that is easier to use.

%description   -n gem-google-apis-slides-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-slides_v1.


%package       -n gem-google-apis-smartdevicemanagement-v1
Version:       0.15.0
Release:       alt1.1
Summary:       Simple REST client for Smart Device Management API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-smartdevicemanagement_v1) = 0.15.0

%description   -n gem-google-apis-smartdevicemanagement-v1
This is the simple REST client for Smart Device Management API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Smart Device Management API,
but note that some services may provide a separate modern client that is easier
to use.


%package       -n gem-google-apis-smartdevicemanagement-v1-doc
Version:       0.15.0
Release:       alt1.1
Summary:       Simple REST client for Smart Device Management API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-smartdevicemanagement_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-smartdevicemanagement_v1) = 0.15.0

%description   -n gem-google-apis-smartdevicemanagement-v1-doc
Simple REST client for Smart Device Management API V1 documentation files.

This is the simple REST client for Smart Device Management API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Smart Device Management API,
but note that some services may provide a separate modern client that is easier
to use.

%description   -n gem-google-apis-smartdevicemanagement-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-smartdevicemanagement_v1.


%package       -n gem-google-apis-smartdevicemanagement-v1-devel
Version:       0.15.0
Release:       alt1.1
Summary:       Simple REST client for Smart Device Management API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-smartdevicemanagement_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-smartdevicemanagement_v1) = 0.15.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-smartdevicemanagement-v1-devel
Simple REST client for Smart Device Management API V1 development package.

This is the simple REST client for Smart Device Management API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Smart Device Management API,
but note that some services may provide a separate modern client that is easier
to use.

%description   -n gem-google-apis-smartdevicemanagement-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-smartdevicemanagement_v1.


%package       -n gem-google-apis-sourcerepo-v1
Version:       0.18.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Source Repositories API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-sourcerepo_v1) = 0.18.0

%description   -n gem-google-apis-sourcerepo-v1
This is the simple REST client for Cloud Source Repositories API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Cloud Source Repositories
API, but note that some services may provide a separate modern client that is
easier to use.


%package       -n gem-google-apis-sourcerepo-v1-doc
Version:       0.18.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Source Repositories API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-sourcerepo_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-sourcerepo_v1) = 0.18.0

%description   -n gem-google-apis-sourcerepo-v1-doc
Simple REST client for Cloud Source Repositories API V1 documentation
files.

This is the simple REST client for Cloud Source Repositories API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Cloud Source Repositories
API, but note that some services may provide a separate modern client that is
easier to use.

%description   -n gem-google-apis-sourcerepo-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-sourcerepo_v1.


%package       -n gem-google-apis-sourcerepo-v1-devel
Version:       0.18.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Source Repositories API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-sourcerepo_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-sourcerepo_v1) = 0.18.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-sourcerepo-v1-devel
Simple REST client for Cloud Source Repositories API V1 development
package.

This is the simple REST client for Cloud Source Repositories API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Cloud Source Repositories
API, but note that some services may provide a separate modern client that is
easier to use.

%description   -n gem-google-apis-sourcerepo-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-sourcerepo_v1.


%package       -n gem-google-apis-spanner-v1
Version:       0.37.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Spanner API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.7 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-spanner_v1) = 0.37.0

%description   -n gem-google-apis-spanner-v1
This is the simple REST client for Cloud Spanner API V1. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Cloud Spanner API, but note that some services may
provide a separate modern client that is easier to use.


%package       -n gem-google-apis-spanner-v1-doc
Version:       0.37.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Spanner API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-spanner_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-spanner_v1) = 0.37.0

%description   -n gem-google-apis-spanner-v1-doc
Simple REST client for Cloud Spanner API V1 documentation files.

This is the simple REST client for Cloud Spanner API V1. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Cloud Spanner API, but note that some services may
provide a separate modern client that is easier to use.

%description   -n gem-google-apis-spanner-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-spanner_v1.


%package       -n gem-google-apis-spanner-v1-devel
Version:       0.37.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Spanner API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-spanner_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-spanner_v1) = 0.37.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-spanner-v1-devel
Simple REST client for Cloud Spanner API V1 development package.

This is the simple REST client for Cloud Spanner API V1. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Cloud Spanner API, but note that some services may
provide a separate modern client that is easier to use.

%description   -n gem-google-apis-spanner-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-spanner_v1.


%package       -n gem-google-apis-speech-v1
Version:       0.26.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Speech-to-Text API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-speech_v1) = 0.26.0

%description   -n gem-google-apis-speech-v1
This is the simple REST client for Cloud Speech-to-Text API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Cloud Speech-to-Text API, but
note that some services may provide a separate modern client that is easier to
use.


%package       -n gem-google-apis-speech-v1-doc
Version:       0.26.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Speech-to-Text API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-speech_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-speech_v1) = 0.26.0

%description   -n gem-google-apis-speech-v1-doc
Simple REST client for Cloud Speech-to-Text API V1 documentation files.

This is the simple REST client for Cloud Speech-to-Text API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Cloud Speech-to-Text API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-speech-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-speech_v1.


%package       -n gem-google-apis-speech-v1-devel
Version:       0.26.0
Release:       alt1.1
Summary:       Simple REST client for Cloud Speech-to-Text API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-speech_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-speech_v1) = 0.26.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-speech-v1-devel
Simple REST client for Cloud Speech-to-Text API V1 development package.

This is the simple REST client for Cloud Speech-to-Text API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Cloud Speech-to-Text API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-speech-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-speech_v1.


%package       -n gem-google-apis-sqladmin-v1
Version:       0.27.0
Release:       alt1.1
Summary:       Simple REST client for Cloud SQL Admin API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-sqladmin_v1) = 0.27.0

%description   -n gem-google-apis-sqladmin-v1
This is the simple REST client for Cloud SQL Admin API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Cloud SQL Admin API, but note that some
services may provide a separate modern client that is easier to use.


%package       -n gem-google-apis-sqladmin-v1-doc
Version:       0.27.0
Release:       alt1.1
Summary:       Simple REST client for Cloud SQL Admin API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-sqladmin_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-sqladmin_v1) = 0.27.0

%description   -n gem-google-apis-sqladmin-v1-doc
Simple REST client for Cloud SQL Admin API V1 documentation files.

This is the simple REST client for Cloud SQL Admin API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Cloud SQL Admin API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-sqladmin-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-sqladmin_v1.


%package       -n gem-google-apis-sqladmin-v1-devel
Version:       0.27.0
Release:       alt1.1
Summary:       Simple REST client for Cloud SQL Admin API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-sqladmin_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-sqladmin_v1) = 0.27.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-sqladmin-v1-devel
Simple REST client for Cloud SQL Admin API V1 development package.

This is the simple REST client for Cloud SQL Admin API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Cloud SQL Admin API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-sqladmin-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-sqladmin_v1.


%package       -n gem-google-apis-sqladmin-v1beta4
Version:       0.38.0
Release:       alt1.1
Summary:       Simple REST client for Cloud SQL Admin API V1beta4
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-sqladmin_v1beta4) = 0.38.0

%description   -n gem-google-apis-sqladmin-v1beta4
This is the simple REST client for Cloud SQL Admin API V1beta4. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Cloud SQL Admin API, but note
that some services may provide a separate modern client that is easier to use.


%package       -n gem-google-apis-sqladmin-v1beta4-doc
Version:       0.38.0
Release:       alt1.1
Summary:       Simple REST client for Cloud SQL Admin API V1beta4 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-sqladmin_v1beta4
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-sqladmin_v1beta4) = 0.38.0

%description   -n gem-google-apis-sqladmin-v1beta4-doc
Simple REST client for Cloud SQL Admin API V1beta4 documentation files.

This is the simple REST client for Cloud SQL Admin API V1beta4. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Cloud SQL Admin API, but note
that some services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-sqladmin-v1beta4-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-sqladmin_v1beta4.


%package       -n gem-google-apis-sqladmin-v1beta4-devel
Version:       0.38.0
Release:       alt1.1
Summary:       Simple REST client for Cloud SQL Admin API V1beta4 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-sqladmin_v1beta4
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-sqladmin_v1beta4) = 0.38.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-sqladmin-v1beta4-devel
Simple REST client for Cloud SQL Admin API V1beta4 development package.

This is the simple REST client for Cloud SQL Admin API V1beta4. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Cloud SQL Admin API, but note
that some services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-sqladmin-v1beta4-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-sqladmin_v1beta4.


%package       -n gem-google-apis-storage-v1
Version:       0.19.0
Release:       alt1.1
Summary:       REST client for Google APIs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-storage_v1) = 0.19.0

%description   -n gem-google-apis-storage-v1
REST client for Google APIs.


%package       -n gem-google-apis-storage-v1-doc
Version:       0.19.0
Release:       alt1.1
Summary:       REST client for Google APIs documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-storage_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-storage_v1) = 0.19.0

%description   -n gem-google-apis-storage-v1-doc
REST client for Google APIs documentation files.

%description   -n gem-google-apis-storage-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-storage_v1.


%package       -n gem-google-apis-storage-v1-devel
Version:       0.19.0
Release:       alt1.1
Summary:       REST client for Google APIs development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-storage_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-storage_v1) = 0.19.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-storage-v1-devel
REST client for Google APIs development package.

%description   -n gem-google-apis-storage-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-storage_v1.


%package       -n gem-google-apis-storagetransfer-v1
Version:       0.34.0
Release:       alt1.1
Summary:       Simple REST client for Storage Transfer API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-storagetransfer_v1) = 0.34.0

%description   -n gem-google-apis-storagetransfer-v1
This is the simple REST client for Storage Transfer API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Storage Transfer API, but note that some
services may provide a separate modern client that is easier to use.


%package       -n gem-google-apis-storagetransfer-v1-doc
Version:       0.34.0
Release:       alt1.1
Summary:       Simple REST client for Storage Transfer API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-storagetransfer_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-storagetransfer_v1) = 0.34.0

%description   -n gem-google-apis-storagetransfer-v1-doc
Simple REST client for Storage Transfer API V1 documentation files.

This is the simple REST client for Storage Transfer API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Storage Transfer API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-storagetransfer-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-storagetransfer_v1.


%package       -n gem-google-apis-storagetransfer-v1-devel
Version:       0.34.0
Release:       alt1.1
Summary:       Simple REST client for Storage Transfer API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-storagetransfer_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-storagetransfer_v1) = 0.34.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-storagetransfer-v1-devel
Simple REST client for Storage Transfer API V1 development package.

This is the simple REST client for Storage Transfer API V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the Storage Transfer API, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-storagetransfer-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-storagetransfer_v1.


%package       -n gem-google-apis-streetviewpublish-v1
Version:       0.23.0
Release:       alt1.1
Summary:       Simple REST client for Street View Publish API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-streetviewpublish_v1) = 0.23.0

%description   -n gem-google-apis-streetviewpublish-v1
This is the simple REST client for Street View Publish API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Street View Publish API, but
note that some services may provide a separate modern client that is easier to
use.


%package       -n gem-google-apis-streetviewpublish-v1-doc
Version:       0.23.0
Release:       alt1.1
Summary:       Simple REST client for Street View Publish API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-streetviewpublish_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-streetviewpublish_v1) = 0.23.0

%description   -n gem-google-apis-streetviewpublish-v1-doc
Simple REST client for Street View Publish API V1 documentation files.

This is the simple REST client for Street View Publish API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Street View Publish API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-streetviewpublish-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-streetviewpublish_v1.


%package       -n gem-google-apis-streetviewpublish-v1-devel
Version:       0.23.0
Release:       alt1.1
Summary:       Simple REST client for Street View Publish API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-streetviewpublish_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-streetviewpublish_v1) = 0.23.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-streetviewpublish-v1-devel
Simple REST client for Street View Publish API V1 development package.

This is the simple REST client for Street View Publish API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Street View Publish API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-streetviewpublish-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-streetviewpublish_v1.


%package       -n gem-google-apis-sts-v1
Version:       0.24.0
Release:       alt1.1
Summary:       Simple REST client for Security Token Service API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-sts_v1) = 0.24.0

%description   -n gem-google-apis-sts-v1
This is the simple REST client for Security Token Service API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Security Token Service API,
but note that some services may provide a separate modern client that is easier
to use.


%package       -n gem-google-apis-sts-v1-doc
Version:       0.24.0
Release:       alt1.1
Summary:       Simple REST client for Security Token Service API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-sts_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-sts_v1) = 0.24.0

%description   -n gem-google-apis-sts-v1-doc
Simple REST client for Security Token Service API V1 documentation files.

This is the simple REST client for Security Token Service API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Security Token Service API,
but note that some services may provide a separate modern client that is easier
to use.

%description   -n gem-google-apis-sts-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-sts_v1.


%package       -n gem-google-apis-sts-v1-devel
Version:       0.24.0
Release:       alt1.1
Summary:       Simple REST client for Security Token Service API V1 development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-sts_v1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-sts_v1) = 0.24.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-sts-v1-devel
Simple REST client for Security Token Service API V1 development package.

This is the simple REST client for Security Token Service API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Security Token Service API,
but note that some services may provide a separate modern client that is easier
to use.

%description   -n gem-google-apis-sts-v1-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-sts_v1.


%package       -n gem-google-apis-sts-v1beta
Version:       0.20.0
Release:       alt1.1
Summary:       Simple REST client for Security Token Service API V1beta
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Provides:      gem(google-apis-sts_v1beta) = 0.20.0

%description   -n gem-google-apis-sts-v1beta
This is the simple REST client for Security Token Service API V1beta. Simple
REST clients are Ruby client libraries that provide access to Google services
via their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Security Token Service API,
but note that some services may provide a separate modern client that is easier
to use.


%package       -n gem-google-apis-sts-v1beta-doc
Version:       0.20.0
Release:       alt1.1
Summary:       Simple REST client for Security Token Service API V1beta documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-sts_v1beta
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-sts_v1beta) = 0.20.0

%description   -n gem-google-apis-sts-v1beta-doc
Simple REST client for Security Token Service API V1beta documentation
files.

This is the simple REST client for Security Token Service API V1beta. Simple
REST clients are Ruby client libraries that provide access to Google services
via their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Security Token Service API,
but note that some services may provide a separate modern client that is easier
to use.

%description   -n gem-google-apis-sts-v1beta-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-sts_v1beta.


%package       -n gem-google-apis-sts-v1beta-devel
Version:       0.20.0
Release:       alt1.1
Summary:       Simple REST client for Security Token Service API V1beta development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-sts_v1beta
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-sts_v1beta) = 0.20.0
Requires:      gem(bundler) >= 1.17
Requires:      gem(rake) >= 12.0
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4
Requires:      gem(opencensus) >= 0.5 gem(opencensus) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.5 gem(redcarpet) < 4

%description   -n gem-google-apis-sts-v1beta-devel
Simple REST client for Security Token Service API V1beta development
package.

This is the simple REST client for Security Token Service API V1beta. Simple
REST clients are Ruby client libraries that provide access to Google services
via their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Security Token Service API,
but note that some services may provide a separate modern client that is easier
to use.

%description   -n gem-google-apis-sts-v1beta-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-sts_v1beta.


%package       -n gem-google-api-client
Version:       0.53.0
Release:       alt1.1
Summary:       REST client for Google APIs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.1 gem(google-apis-core) < 1
Requires:      gem(google-apis-generator) >= 0.1 gem(google-apis-generator) < 1
Obsoletes:     ruby-google-api < %EVR
Provides:      ruby-google-api = %EVR
Provides:      gem(google-api-client) = 0.53.0

%description   -n gem-google-api-client
REST client for Google APIs.


%package       -n gem-google-api-client-doc
Version:       0.53.0
Release:       alt1.1
Summary:       REST client for Google APIs documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-api-client
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-api-client) = 0.53.0

%description   -n gem-google-api-client-doc
REST client for Google APIs documentation files.

%description   -n gem-google-api-client-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-api-client.


%package       -n gem-google-api-client-devel
Version:       0.53.0
Release:       alt1.1
Summary:       REST client for Google APIs development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-api-client
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-api-client) = 0.53.0
Requires:      gem(bundler) >= 1.7
Requires:      gem(rake) >= 13.0 gem(rake) < 14
Requires:      gem(rspec) >= 3.1 gem(rspec) < 4
Requires:      gem(json_spec) >= 1.1 gem(json_spec) < 2
Requires:      gem(webmock) >= 3.0 gem(webmock) < 4
Requires:      gem(simplecov) >= 0.12 gem(simplecov) < 1
Requires:      gem(coveralls) >= 0.8 gem(coveralls) < 1
Requires:      gem(rubocop) >= 0.49.0 gem(rubocop) < 2
Requires:      gem(launchy) >= 2.4 gem(launchy) < 3
Requires:      gem(dotenv) >= 2.0 gem(dotenv) < 3
Requires:      gem(fakefs) >= 1.0 gem(fakefs) < 2
Requires:      gem(google-id-token) >= 1.3 gem(google-id-token) < 2
Requires:      gem(os) >= 0.9 gem(os) < 2
Requires:      gem(rmail) >= 1.1 gem(rmail) < 2
Requires:      gem(redis) >= 3.2 gem(redis) < 6
Requires:      gem(logging) >= 2.2 gem(logging) < 3
Requires:      gem(opencensus) >= 0.4 gem(opencensus) < 1
Requires:      gem(httparty) >= 0
Requires:      gem(gems) >= 1.2 gem(gems) < 2
Requires:      gem(yard) >= 0.9.11 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.2 gem(redcarpet) < 4
Requires:      gem(github-markup) >= 1.3 gem(github-markup) < 5
Requires:      gem(pry-doc) >= 0.8 gem(pry-doc) < 2
Requires:      gem(pry-byebug) >= 3.2 gem(pry-byebug) < 4

%description   -n gem-google-api-client-devel
REST client for Google APIs development package.

%description   -n gem-google-api-client-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-api-client.


%package       -n gem-google-apis-core
Version:       0.9.0
Release:       alt1.1
Summary:       REST client for Google APIs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(representable) >= 3.0 gem(representable) < 4
Requires:      gem(retriable) >= 2.0 gem(retriable) < 4.a
Requires:      gem(addressable) >= 2.5.1 gem(addressable) < 3
Requires:      gem(mini_mime) >= 1.0 gem(mini_mime) < 2
Requires:      gem(googleauth) >= 0.16.2 gem(googleauth) < 2.a
Requires:      gem(httpclient) >= 2.8.1 gem(httpclient) < 3.a
Requires:      gem(rexml) >= 0
Requires:      gem(webrick) >= 0
Provides:      gem(google-apis-core) = 0.9.0

%description   -n gem-google-apis-core
REST client for Google APIs.


%package       -n gem-google-apis-core-doc
Version:       0.9.0
Release:       alt1.1
Summary:       REST client for Google APIs documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-core
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-core) = 0.9.0

%description   -n gem-google-apis-core-doc
REST client for Google APIs documentation files.

%description   -n gem-google-apis-core-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-core.


%package       -n gem-google-apis-core-devel
Version:       0.9.0
Release:       alt1.1
Summary:       REST client for Google APIs development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-core
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) = 0.9.0
Requires:      gem(bundler) >= 1.7
Requires:      gem(rake) >= 13.0 gem(rake) < 14
Requires:      gem(rspec) >= 3.1 gem(rspec) < 4
Requires:      gem(json_spec) >= 1.1 gem(json_spec) < 2
Requires:      gem(webmock) >= 3.0 gem(webmock) < 4
Requires:      gem(rubocop) >= 0.49.0 gem(rubocop) < 2
Requires:      gem(launchy) >= 2.4 gem(launchy) < 3
Requires:      gem(dotenv) >= 2.0 gem(dotenv) < 3
Requires:      gem(fakefs) >= 1.0 gem(fakefs) < 2
Requires:      gem(google-id-token) >= 1.3 gem(google-id-token) < 2
Requires:      gem(os) >= 0.9 gem(os) < 2
Requires:      gem(rmail) >= 1.1 gem(rmail) < 2
Requires:      gem(redis) >= 3.2 gem(redis) < 6
Requires:      gem(logging) >= 2.2 gem(logging) < 3
Requires:      gem(opencensus) >= 0.4 gem(opencensus) < 1
Requires:      gem(httparty) >= 0
Requires:      gem(yard) >= 0.9.11 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.2 gem(redcarpet) < 4
Requires:      gem(github-markup) >= 1.3 gem(github-markup) < 5
Requires:      gem(pry-doc) >= 0.8 gem(pry-doc) < 2
Requires:      gem(pry-byebug) >= 3.2 gem(pry-byebug) < 4

%description   -n gem-google-apis-core-devel
REST client for Google APIs development package.

%description   -n gem-google-apis-core-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-core.


%package       -n gem-google-apis-generator
Version:       0.10.0
Release:       alt1.1
Summary:       REST client for Google APIs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activesupport) >= 5.0
Requires:      gem(gems) >= 1.2 gem(gems) < 2
Requires:      gem(google-apis-core) >= 0.9.0 gem(google-apis-core) < 2.a
Requires:      gem(google-apis-discovery_v1) >= 0.5 gem(google-apis-discovery_v1) < 1
Requires:      gem(thor) >= 0.20 gem(thor) < 2.a
Provides:      gem(google-apis-generator) = 0.10.0

%description   -n gem-google-apis-generator
REST client for Google APIs.


%package       -n generate-api
Version:       0.10.0
Release:       alt1.1
Summary:       REST client for Google APIs executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета google-apis-generator
Group:         Other
BuildArch:     noarch

Requires:      gem(google-apis-generator) = 0.10.0

%description   -n generate-api
REST client for Google APIs executable(s).

%description   -n generate-api -l ru_RU.UTF-8
Исполнямка для самоцвета google-apis-generator.


%package       -n gem-google-apis-generator-doc
Version:       0.10.0
Release:       alt1.1
Summary:       REST client for Google APIs documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-generator
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-generator) = 0.10.0

%description   -n gem-google-apis-generator-doc
REST client for Google APIs documentation files.

%description   -n gem-google-apis-generator-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-generator.


%package       -n gem-google-apis-generator-devel
Version:       0.10.0
Release:       alt1.1
Summary:       REST client for Google APIs development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета google-apis-generator
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-generator) = 0.10.0
Requires:      gem(bundler) >= 1.7
Requires:      gem(rake) >= 13.0 gem(rake) < 14
Requires:      gem(rspec) >= 3.1 gem(rspec) < 4
Requires:      gem(json_spec) >= 1.1 gem(json_spec) < 2
Requires:      gem(webmock) >= 3.0 gem(webmock) < 4
Requires:      gem(rubocop) >= 0.49.0 gem(rubocop) < 2
Requires:      gem(launchy) >= 2.4 gem(launchy) < 3
Requires:      gem(dotenv) >= 2.0 gem(dotenv) < 3
Requires:      gem(fakefs) >= 1.0 gem(fakefs) < 2
Requires:      gem(google-id-token) >= 1.3 gem(google-id-token) < 2
Requires:      gem(os) >= 0.9 gem(os) < 2
Requires:      gem(rmail) >= 1.1 gem(rmail) < 2
Requires:      gem(redis) >= 3.2 gem(redis) < 6
Requires:      gem(logging) >= 2.2 gem(logging) < 3
Requires:      gem(opencensus) >= 0.4 gem(opencensus) < 1
Requires:      gem(httparty) >= 0
Requires:      gem(yard) >= 0.9.11 gem(yard) < 1
Requires:      gem(redcarpet) >= 3.2 gem(redcarpet) < 4
Requires:      gem(github-markup) >= 1.3 gem(github-markup) < 5
Requires:      gem(pry-doc) >= 0.8 gem(pry-doc) < 2
Requires:      gem(pry-byebug) >= 3.2 gem(pry-byebug) < 4

%description   -n gem-google-apis-generator-devel
REST client for Google APIs development package.

%description   -n gem-google-apis-generator-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета google-apis-generator.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files

%files         -n gem-google-apis-baremetalsolution-v1
%ruby_gemspecdir/google-apis-baremetalsolution_v1-0.13.0.gemspec
%ruby_gemslibdir/google-apis-baremetalsolution_v1-0.13.0

%files         -n gem-google-apis-baremetalsolution-v1-doc
%ruby_gemsdocdir/google-apis-baremetalsolution_v1-0.13.0

%files         -n gem-google-apis-baremetalsolution-v1-devel

%files         -n gem-google-apis-baremetalsolution-v2
%ruby_gemspecdir/google-apis-baremetalsolution_v2-0.24.0.gemspec
%ruby_gemslibdir/google-apis-baremetalsolution_v2-0.24.0

%files         -n gem-google-apis-baremetalsolution-v2-doc
%ruby_gemsdocdir/google-apis-baremetalsolution_v2-0.24.0

%files         -n gem-google-apis-baremetalsolution-v2-devel

%files         -n gem-google-apis-beyondcorp-v1
%ruby_gemspecdir/google-apis-beyondcorp_v1-0.7.0.gemspec
%ruby_gemslibdir/google-apis-beyondcorp_v1-0.7.0

%files         -n gem-google-apis-beyondcorp-v1-doc
%ruby_gemsdocdir/google-apis-beyondcorp_v1-0.7.0

%files         -n gem-google-apis-beyondcorp-v1-devel

%files         -n gem-google-apis-bigquery-v2
%ruby_gemspecdir/google-apis-bigquery_v2-0.42.0.gemspec
%ruby_gemslibdir/google-apis-bigquery_v2-0.42.0

%files         -n gem-google-apis-bigquery-v2-doc
%ruby_gemsdocdir/google-apis-bigquery_v2-0.42.0

%files         -n gem-google-apis-bigquery-v2-devel

%files         -n gem-google-apis-bigquerydatatransfer-v1
%ruby_gemspecdir/google-apis-bigquerydatatransfer_v1-0.28.0.gemspec
%ruby_gemslibdir/google-apis-bigquerydatatransfer_v1-0.28.0

%files         -n gem-google-apis-bigquerydatatransfer-v1-doc
%ruby_gemsdocdir/google-apis-bigquerydatatransfer_v1-0.28.0

%files         -n gem-google-apis-bigquerydatatransfer-v1-devel

%files         -n gem-google-apis-bigqueryreservation-v1
%ruby_gemspecdir/google-apis-bigqueryreservation_v1-0.21.0.gemspec
%ruby_gemslibdir/google-apis-bigqueryreservation_v1-0.21.0

%files         -n gem-google-apis-bigqueryreservation-v1-doc
%ruby_gemsdocdir/google-apis-bigqueryreservation_v1-0.21.0

%files         -n gem-google-apis-bigqueryreservation-v1-devel

%files         -n gem-google-apis-bigtableadmin-v1
%ruby_gemspecdir/google-apis-bigtableadmin_v1-0.11.0.gemspec
%ruby_gemslibdir/google-apis-bigtableadmin_v1-0.11.0

%files         -n gem-google-apis-bigtableadmin-v1-doc
%ruby_gemsdocdir/google-apis-bigtableadmin_v1-0.11.0

%files         -n gem-google-apis-bigtableadmin-v1-devel

%files         -n gem-google-apis-bigtableadmin-v2
%ruby_gemspecdir/google-apis-bigtableadmin_v2-0.29.0.gemspec
%ruby_gemslibdir/google-apis-bigtableadmin_v2-0.29.0

%files         -n gem-google-apis-bigtableadmin-v2-doc
%ruby_gemsdocdir/google-apis-bigtableadmin_v2-0.29.0

%files         -n gem-google-apis-bigtableadmin-v2-devel

%files         -n gem-google-apis-billingbudgets-v1
%ruby_gemspecdir/google-apis-billingbudgets_v1-0.21.0.gemspec
%ruby_gemslibdir/google-apis-billingbudgets_v1-0.21.0

%files         -n gem-google-apis-billingbudgets-v1-doc
%ruby_gemsdocdir/google-apis-billingbudgets_v1-0.21.0

%files         -n gem-google-apis-billingbudgets-v1-devel

%files         -n gem-google-apis-binaryauthorization-v1
%ruby_gemspecdir/google-apis-binaryauthorization_v1-0.23.0.gemspec
%ruby_gemslibdir/google-apis-binaryauthorization_v1-0.23.0

%files         -n gem-google-apis-binaryauthorization-v1-doc
%ruby_gemsdocdir/google-apis-binaryauthorization_v1-0.23.0

%files         -n gem-google-apis-binaryauthorization-v1-devel

%files         -n gem-google-apis-blogger-v2
%ruby_gemspecdir/google-apis-blogger_v2-0.12.0.gemspec
%ruby_gemslibdir/google-apis-blogger_v2-0.12.0

%files         -n gem-google-apis-blogger-v2-doc
%ruby_gemsdocdir/google-apis-blogger_v2-0.12.0

%files         -n gem-google-apis-blogger-v2-devel

%files         -n gem-google-apis-blogger-v3
%ruby_gemspecdir/google-apis-blogger_v3-0.12.0.gemspec
%ruby_gemslibdir/google-apis-blogger_v3-0.12.0

%files         -n gem-google-apis-blogger-v3-doc
%ruby_gemsdocdir/google-apis-blogger_v3-0.12.0

%files         -n gem-google-apis-blogger-v3-devel

%files         -n gem-google-apis-books-v1
%ruby_gemspecdir/google-apis-books_v1-0.12.0.gemspec
%ruby_gemslibdir/google-apis-books_v1-0.12.0

%files         -n gem-google-apis-books-v1-doc
%ruby_gemsdocdir/google-apis-books_v1-0.12.0

%files         -n gem-google-apis-books-v1-devel

%files         -n gem-google-apis-businessprofileperformance-v1
%ruby_gemspecdir/google-apis-businessprofileperformance_v1-0.4.0.gemspec
%ruby_gemslibdir/google-apis-businessprofileperformance_v1-0.4.0

%files         -n gem-google-apis-businessprofileperformance-v1-doc
%ruby_gemsdocdir/google-apis-businessprofileperformance_v1-0.4.0

%files         -n gem-google-apis-businessprofileperformance-v1-devel

%files         -n gem-google-apis-cloudresourcemanager-v1
%ruby_gemspecdir/google-apis-cloudresourcemanager_v1-0.30.0.gemspec
%ruby_gemslibdir/google-apis-cloudresourcemanager_v1-0.30.0

%files         -n gem-google-apis-cloudresourcemanager-v1-doc
%ruby_gemsdocdir/google-apis-cloudresourcemanager_v1-0.30.0

%files         -n gem-google-apis-cloudresourcemanager-v1-devel

%files         -n gem-google-apis-composer-v1
%ruby_gemspecdir/google-apis-composer_v1-0.29.0.gemspec
%ruby_gemslibdir/google-apis-composer_v1-0.29.0

%files         -n gem-google-apis-composer-v1-doc
%ruby_gemsdocdir/google-apis-composer_v1-0.29.0

%files         -n gem-google-apis-composer-v1-devel

%files         -n gem-google-apis-compute-beta
%ruby_gemspecdir/google-apis-compute_beta-0.51.0.gemspec
%ruby_gemslibdir/google-apis-compute_beta-0.51.0

%files         -n gem-google-apis-compute-beta-doc
%ruby_gemsdocdir/google-apis-compute_beta-0.51.0

%files         -n gem-google-apis-compute-beta-devel

%files         -n gem-google-apis-compute-v1
%ruby_gemspecdir/google-apis-compute_v1-0.53.0.gemspec
%ruby_gemslibdir/google-apis-compute_v1-0.53.0

%files         -n gem-google-apis-compute-v1-doc
%ruby_gemsdocdir/google-apis-compute_v1-0.53.0

%files         -n gem-google-apis-compute-v1-devel

%files         -n gem-google-apis-connectors-v1
%ruby_gemspecdir/google-apis-connectors_v1-0.19.0.gemspec
%ruby_gemslibdir/google-apis-connectors_v1-0.19.0

%files         -n gem-google-apis-connectors-v1-doc
%ruby_gemsdocdir/google-apis-connectors_v1-0.19.0

%files         -n gem-google-apis-connectors-v1-devel

%files         -n gem-google-apis-connectors-v2
%ruby_gemspecdir/google-apis-connectors_v2-0.2.0.gemspec
%ruby_gemslibdir/google-apis-connectors_v2-0.2.0

%files         -n gem-google-apis-connectors-v2-doc
%ruby_gemsdocdir/google-apis-connectors_v2-0.2.0

%files         -n gem-google-apis-connectors-v2-devel

%files         -n gem-google-apis-contactcenterinsights-v1
%ruby_gemspecdir/google-apis-contactcenterinsights_v1-0.15.0.gemspec
%ruby_gemslibdir/google-apis-contactcenterinsights_v1-0.15.0

%files         -n gem-google-apis-contactcenterinsights-v1-doc
%ruby_gemsdocdir/google-apis-contactcenterinsights_v1-0.15.0

%files         -n gem-google-apis-contactcenterinsights-v1-devel

%files         -n gem-google-apis-container-v1
%ruby_gemspecdir/google-apis-container_v1-0.37.0.gemspec
%ruby_gemslibdir/google-apis-container_v1-0.37.0

%files         -n gem-google-apis-container-v1-doc
%ruby_gemsdocdir/google-apis-container_v1-0.37.0

%files         -n gem-google-apis-container-v1-devel

%files         -n gem-google-apis-containeranalysis-v1
%ruby_gemspecdir/google-apis-containeranalysis_v1-0.22.0.gemspec
%ruby_gemslibdir/google-apis-containeranalysis_v1-0.22.0

%files         -n gem-google-apis-containeranalysis-v1-doc
%ruby_gemsdocdir/google-apis-containeranalysis_v1-0.22.0

%files         -n gem-google-apis-containeranalysis-v1-devel

%files         -n gem-google-apis-content-v2
%ruby_gemspecdir/google-apis-content_v2-0.17.0.gemspec
%ruby_gemslibdir/google-apis-content_v2-0.17.0

%files         -n gem-google-apis-content-v2-doc
%ruby_gemsdocdir/google-apis-content_v2-0.17.0

%files         -n gem-google-apis-content-v2-devel

%files         -n gem-google-apis-content-v2-1
%ruby_gemspecdir/google-apis-content_v2_1-0.31.0.gemspec
%ruby_gemslibdir/google-apis-content_v2_1-0.31.0

%files         -n gem-google-apis-content-v2-1-doc
%ruby_gemsdocdir/google-apis-content_v2_1-0.31.0

%files         -n gem-google-apis-content-v2-1-devel

%files         -n gem-google-apis-contentwarehouse-v1
%ruby_gemspecdir/google-apis-contentwarehouse_v1-0.1.0.gemspec
%ruby_gemslibdir/google-apis-contentwarehouse_v1-0.1.0

%files         -n gem-google-apis-contentwarehouse-v1-doc
%ruby_gemsdocdir/google-apis-contentwarehouse_v1-0.1.0

%files         -n gem-google-apis-contentwarehouse-v1-devel

%files         -n gem-google-apis-discovery-v1
%ruby_gemspecdir/google-apis-discovery_v1-0.12.0.gemspec
%ruby_gemslibdir/google-apis-discovery_v1-0.12.0

%files         -n gem-google-apis-discovery-v1-doc
%ruby_gemsdocdir/google-apis-discovery_v1-0.12.0

%files         -n gem-google-apis-discovery-v1-devel

%files         -n gem-google-apis-dns-v1
%ruby_gemspecdir/google-apis-dns_v1-0.28.0.gemspec
%ruby_gemslibdir/google-apis-dns_v1-0.28.0

%files         -n gem-google-apis-dns-v1-doc
%ruby_gemsdocdir/google-apis-dns_v1-0.28.0

%files         -n gem-google-apis-dns-v1-devel

%files         -n gem-google-apis-dns-v2
%ruby_gemspecdir/google-apis-dns_v2-0.1.0.gemspec
%ruby_gemslibdir/google-apis-dns_v2-0.1.0

%files         -n gem-google-apis-dns-v2-doc
%ruby_gemsdocdir/google-apis-dns_v2-0.1.0

%files         -n gem-google-apis-dns-v2-devel

%files         -n gem-google-apis-iam-v1
%ruby_gemspecdir/google-apis-iam_v1-0.35.0.gemspec
%ruby_gemslibdir/google-apis-iam_v1-0.35.0

%files         -n gem-google-apis-iam-v1-doc
%ruby_gemsdocdir/google-apis-iam_v1-0.35.0

%files         -n gem-google-apis-iam-v1-devel

%files         -n gem-google-apis-iam-v2beta
%ruby_gemspecdir/google-apis-iam_v2beta-0.7.0.gemspec
%ruby_gemslibdir/google-apis-iam_v2beta-0.7.0

%files         -n gem-google-apis-iam-v2beta-doc
%ruby_gemsdocdir/google-apis-iam_v2beta-0.7.0

%files         -n gem-google-apis-iam-v2beta-devel

%files         -n gem-google-apis-iamcredentials-v1
%ruby_gemspecdir/google-apis-iamcredentials_v1-0.15.0.gemspec
%ruby_gemslibdir/google-apis-iamcredentials_v1-0.15.0

%files         -n gem-google-apis-iamcredentials-v1-doc
%ruby_gemsdocdir/google-apis-iamcredentials_v1-0.15.0

%files         -n gem-google-apis-iamcredentials-v1-devel

%files         -n gem-google-apis-iap-v1
%ruby_gemspecdir/google-apis-iap_v1-0.27.0.gemspec
%ruby_gemslibdir/google-apis-iap_v1-0.27.0

%files         -n gem-google-apis-iap-v1-doc
%ruby_gemsdocdir/google-apis-iap_v1-0.27.0

%files         -n gem-google-apis-iap-v1-devel

%files         -n gem-google-apis-ideahub-v1beta
%ruby_gemspecdir/google-apis-ideahub_v1beta-0.9.0.gemspec
%ruby_gemslibdir/google-apis-ideahub_v1beta-0.9.0

%files         -n gem-google-apis-ideahub-v1beta-doc
%ruby_gemsdocdir/google-apis-ideahub_v1beta-0.9.0

%files         -n gem-google-apis-ideahub-v1beta-devel

%files         -n gem-google-apis-identitytoolkit-v2
%ruby_gemspecdir/google-apis-identitytoolkit_v2-0.3.0.gemspec
%ruby_gemslibdir/google-apis-identitytoolkit_v2-0.3.0

%files         -n gem-google-apis-identitytoolkit-v2-doc
%ruby_gemsdocdir/google-apis-identitytoolkit_v2-0.3.0

%files         -n gem-google-apis-identitytoolkit-v2-devel

%files         -n gem-google-apis-identitytoolkit-v3
%ruby_gemspecdir/google-apis-identitytoolkit_v3-0.12.0.gemspec
%ruby_gemslibdir/google-apis-identitytoolkit_v3-0.12.0

%files         -n gem-google-apis-identitytoolkit-v3-doc
%ruby_gemsdocdir/google-apis-identitytoolkit_v3-0.12.0

%files         -n gem-google-apis-identitytoolkit-v3-devel

%files         -n gem-google-apis-ids-v1
%ruby_gemspecdir/google-apis-ids_v1-0.8.0.gemspec
%ruby_gemslibdir/google-apis-ids_v1-0.8.0

%files         -n gem-google-apis-ids-v1-doc
%ruby_gemsdocdir/google-apis-ids_v1-0.8.0

%files         -n gem-google-apis-ids-v1-devel

%files         -n gem-google-apis-indexing-v3
%ruby_gemspecdir/google-apis-indexing_v3-0.11.0.gemspec
%ruby_gemslibdir/google-apis-indexing_v3-0.11.0

%files         -n gem-google-apis-indexing-v3-doc
%ruby_gemsdocdir/google-apis-indexing_v3-0.11.0

%files         -n gem-google-apis-indexing-v3-devel

%files         -n gem-google-apis-managedidentities-v1
%ruby_gemspecdir/google-apis-managedidentities_v1-0.25.0.gemspec
%ruby_gemslibdir/google-apis-managedidentities_v1-0.25.0

%files         -n gem-google-apis-managedidentities-v1-doc
%ruby_gemsdocdir/google-apis-managedidentities_v1-0.25.0

%files         -n gem-google-apis-managedidentities-v1-devel

%files         -n gem-google-apis-manufacturers-v1
%ruby_gemspecdir/google-apis-manufacturers_v1-0.16.0.gemspec
%ruby_gemslibdir/google-apis-manufacturers_v1-0.16.0

%files         -n gem-google-apis-manufacturers-v1-doc
%ruby_gemsdocdir/google-apis-manufacturers_v1-0.16.0

%files         -n gem-google-apis-manufacturers-v1-devel

%files         -n gem-google-apis-memcache-v1
%ruby_gemspecdir/google-apis-memcache_v1-0.25.0.gemspec
%ruby_gemslibdir/google-apis-memcache_v1-0.25.0

%files         -n gem-google-apis-memcache-v1-doc
%ruby_gemsdocdir/google-apis-memcache_v1-0.25.0

%files         -n gem-google-apis-memcache-v1-devel

%files         -n gem-google-apis-metastore-v1beta
%ruby_gemspecdir/google-apis-metastore_v1beta-0.37.0.gemspec
%ruby_gemslibdir/google-apis-metastore_v1beta-0.37.0

%files         -n gem-google-apis-metastore-v1beta-doc
%ruby_gemsdocdir/google-apis-metastore_v1beta-0.37.0

%files         -n gem-google-apis-metastore-v1beta-devel

%files         -n gem-google-apis-ml-v1
%ruby_gemspecdir/google-apis-ml_v1-0.28.0.gemspec
%ruby_gemslibdir/google-apis-ml_v1-0.28.0

%files         -n gem-google-apis-ml-v1-doc
%ruby_gemsdocdir/google-apis-ml_v1-0.28.0

%files         -n gem-google-apis-ml-v1-devel

%files         -n gem-google-apis-monitoring-v1
%ruby_gemspecdir/google-apis-monitoring_v1-0.29.0.gemspec
%ruby_gemslibdir/google-apis-monitoring_v1-0.29.0

%files         -n gem-google-apis-monitoring-v1-doc
%ruby_gemsdocdir/google-apis-monitoring_v1-0.29.0

%files         -n gem-google-apis-monitoring-v1-devel

%files         -n gem-google-apis-monitoring-v3
%ruby_gemspecdir/google-apis-monitoring_v3-0.36.0.gemspec
%ruby_gemslibdir/google-apis-monitoring_v3-0.36.0

%files         -n gem-google-apis-monitoring-v3-doc
%ruby_gemsdocdir/google-apis-monitoring_v3-0.36.0

%files         -n gem-google-apis-monitoring-v3-devel

%files         -n gem-google-apis-mybusinessaccountmanagement-v1
%ruby_gemspecdir/google-apis-mybusinessaccountmanagement_v1-0.18.0.gemspec
%ruby_gemslibdir/google-apis-mybusinessaccountmanagement_v1-0.18.0

%files         -n gem-google-apis-mybusinessaccountmanagement-v1-doc
%ruby_gemsdocdir/google-apis-mybusinessaccountmanagement_v1-0.18.0

%files         -n gem-google-apis-mybusinessaccountmanagement-v1-devel

%files         -n gem-google-apis-mybusinessbusinesscalls-v1
%ruby_gemspecdir/google-apis-mybusinessbusinesscalls_v1-0.6.0.gemspec
%ruby_gemslibdir/google-apis-mybusinessbusinesscalls_v1-0.6.0

%files         -n gem-google-apis-mybusinessbusinesscalls-v1-doc
%ruby_gemsdocdir/google-apis-mybusinessbusinesscalls_v1-0.6.0

%files         -n gem-google-apis-mybusinessbusinesscalls-v1-devel

%files         -n gem-google-apis-mybusinessbusinessinformation-v1
%ruby_gemspecdir/google-apis-mybusinessbusinessinformation_v1-0.13.0.gemspec
%ruby_gemslibdir/google-apis-mybusinessbusinessinformation_v1-0.13.0

%files         -n gem-google-apis-mybusinessbusinessinformation-v1-doc
%ruby_gemsdocdir/google-apis-mybusinessbusinessinformation_v1-0.13.0

%files         -n gem-google-apis-mybusinessbusinessinformation-v1-devel

%files         -n gem-google-apis-mybusinesslodging-v1
%ruby_gemspecdir/google-apis-mybusinesslodging_v1-0.12.0.gemspec
%ruby_gemslibdir/google-apis-mybusinesslodging_v1-0.12.0

%files         -n gem-google-apis-mybusinesslodging-v1-doc
%ruby_gemsdocdir/google-apis-mybusinesslodging_v1-0.12.0

%files         -n gem-google-apis-mybusinesslodging-v1-devel

%files         -n gem-google-apis-mybusinessnotifications-v1
%ruby_gemspecdir/google-apis-mybusinessnotifications_v1-0.8.0.gemspec
%ruby_gemslibdir/google-apis-mybusinessnotifications_v1-0.8.0

%files         -n gem-google-apis-mybusinessnotifications-v1-doc
%ruby_gemsdocdir/google-apis-mybusinessnotifications_v1-0.8.0

%files         -n gem-google-apis-mybusinessnotifications-v1-devel

%files         -n gem-google-apis-mybusinessplaceactions-v1
%ruby_gemspecdir/google-apis-mybusinessplaceactions_v1-0.13.0.gemspec
%ruby_gemslibdir/google-apis-mybusinessplaceactions_v1-0.13.0

%files         -n gem-google-apis-mybusinessplaceactions-v1-doc
%ruby_gemsdocdir/google-apis-mybusinessplaceactions_v1-0.13.0

%files         -n gem-google-apis-mybusinessplaceactions-v1-devel

%files         -n gem-google-apis-mybusinessqanda-v1
%ruby_gemspecdir/google-apis-mybusinessqanda_v1-0.7.0.gemspec
%ruby_gemslibdir/google-apis-mybusinessqanda_v1-0.7.0

%files         -n gem-google-apis-mybusinessqanda-v1-doc
%ruby_gemsdocdir/google-apis-mybusinessqanda_v1-0.7.0

%files         -n gem-google-apis-mybusinessqanda-v1-devel

%files         -n gem-google-apis-mybusinessverifications-v1
%ruby_gemspecdir/google-apis-mybusinessverifications_v1-0.10.0.gemspec
%ruby_gemslibdir/google-apis-mybusinessverifications_v1-0.10.0

%files         -n gem-google-apis-mybusinessverifications-v1-doc
%ruby_gemsdocdir/google-apis-mybusinessverifications_v1-0.10.0

%files         -n gem-google-apis-mybusinessverifications-v1-devel

%files         -n gem-google-apis-pagespeedonline-v5
%ruby_gemspecdir/google-apis-pagespeedonline_v5-0.13.0.gemspec
%ruby_gemslibdir/google-apis-pagespeedonline_v5-0.13.0

%files         -n gem-google-apis-pagespeedonline-v5-doc
%ruby_gemsdocdir/google-apis-pagespeedonline_v5-0.13.0

%files         -n gem-google-apis-pagespeedonline-v5-devel

%files         -n gem-google-apis-paymentsresellersubscription-v1
%ruby_gemspecdir/google-apis-paymentsresellersubscription_v1-0.22.0.gemspec
%ruby_gemslibdir/google-apis-paymentsresellersubscription_v1-0.22.0

%files         -n gem-google-apis-paymentsresellersubscription-v1-doc
%ruby_gemsdocdir/google-apis-paymentsresellersubscription_v1-0.22.0

%files         -n gem-google-apis-paymentsresellersubscription-v1-devel

%files         -n gem-google-apis-people-v1
%ruby_gemspecdir/google-apis-people_v1-0.33.0.gemspec
%ruby_gemslibdir/google-apis-people_v1-0.33.0

%files         -n gem-google-apis-people-v1-doc
%ruby_gemsdocdir/google-apis-people_v1-0.33.0

%files         -n gem-google-apis-people-v1-devel

%files         -n gem-google-apis-playablelocations-v3
%ruby_gemspecdir/google-apis-playablelocations_v3-0.6.0.gemspec
%ruby_gemslibdir/google-apis-playablelocations_v3-0.6.0

%files         -n gem-google-apis-playablelocations-v3-doc
%ruby_gemsdocdir/google-apis-playablelocations_v3-0.6.0

%files         -n gem-google-apis-playablelocations-v3-devel

%files         -n gem-google-apis-playcustomapp-v1
%ruby_gemspecdir/google-apis-playcustomapp_v1-0.11.0.gemspec
%ruby_gemslibdir/google-apis-playcustomapp_v1-0.11.0

%files         -n gem-google-apis-playcustomapp-v1-doc
%ruby_gemsdocdir/google-apis-playcustomapp_v1-0.11.0

%files         -n gem-google-apis-playcustomapp-v1-devel

%files         -n gem-google-apis-playintegrity-v1
%ruby_gemspecdir/google-apis-playintegrity_v1-0.10.0.gemspec
%ruby_gemslibdir/google-apis-playintegrity_v1-0.10.0

%files         -n gem-google-apis-playintegrity-v1-doc
%ruby_gemsdocdir/google-apis-playintegrity_v1-0.10.0

%files         -n gem-google-apis-playintegrity-v1-devel

%files         -n gem-google-apis-policyanalyzer-v1
%ruby_gemspecdir/google-apis-policyanalyzer_v1-0.9.0.gemspec
%ruby_gemslibdir/google-apis-policyanalyzer_v1-0.9.0

%files         -n gem-google-apis-policyanalyzer-v1-doc
%ruby_gemsdocdir/google-apis-policyanalyzer_v1-0.9.0

%files         -n gem-google-apis-policyanalyzer-v1-devel

%files         -n gem-google-apis-policysimulator-v1
%ruby_gemspecdir/google-apis-policysimulator_v1-0.20.0.gemspec
%ruby_gemslibdir/google-apis-policysimulator_v1-0.20.0

%files         -n gem-google-apis-policysimulator-v1-doc
%ruby_gemsdocdir/google-apis-policysimulator_v1-0.20.0

%files         -n gem-google-apis-policysimulator-v1-devel

%files         -n gem-google-apis-policytroubleshooter-v1
%ruby_gemspecdir/google-apis-policytroubleshooter_v1-0.20.0.gemspec
%ruby_gemslibdir/google-apis-policytroubleshooter_v1-0.20.0

%files         -n gem-google-apis-policytroubleshooter-v1-doc
%ruby_gemsdocdir/google-apis-policytroubleshooter_v1-0.20.0

%files         -n gem-google-apis-policytroubleshooter-v1-devel

%files         -n gem-google-apis-policytroubleshooter-v1beta
%ruby_gemspecdir/google-apis-policytroubleshooter_v1beta-0.20.0.gemspec
%ruby_gemslibdir/google-apis-policytroubleshooter_v1beta-0.20.0

%files         -n gem-google-apis-policytroubleshooter-v1beta-doc
%ruby_gemsdocdir/google-apis-policytroubleshooter_v1beta-0.20.0

%files         -n gem-google-apis-policytroubleshooter-v1beta-devel

%files         -n gem-google-apis-poly-v1
%ruby_gemspecdir/google-apis-poly_v1-0.11.0.gemspec
%ruby_gemslibdir/google-apis-poly_v1-0.11.0

%files         -n gem-google-apis-poly-v1-doc
%ruby_gemsdocdir/google-apis-poly_v1-0.11.0

%files         -n gem-google-apis-poly-v1-devel

%files         -n gem-google-apis-privateca-v1
%ruby_gemspecdir/google-apis-privateca_v1-0.25.0.gemspec
%ruby_gemslibdir/google-apis-privateca_v1-0.25.0

%files         -n gem-google-apis-privateca-v1-doc
%ruby_gemsdocdir/google-apis-privateca_v1-0.25.0

%files         -n gem-google-apis-privateca-v1-devel

%files         -n gem-google-apis-pubsub-v1
%ruby_gemspecdir/google-apis-pubsub_v1-0.29.0.gemspec
%ruby_gemslibdir/google-apis-pubsub_v1-0.29.0

%files         -n gem-google-apis-pubsub-v1-doc
%ruby_gemsdocdir/google-apis-pubsub_v1-0.29.0

%files         -n gem-google-apis-pubsub-v1-devel

%files         -n gem-google-apis-pubsublite-v1
%ruby_gemspecdir/google-apis-pubsublite_v1-0.19.0.gemspec
%ruby_gemslibdir/google-apis-pubsublite_v1-0.19.0

%files         -n gem-google-apis-pubsublite-v1-doc
%ruby_gemsdocdir/google-apis-pubsublite_v1-0.19.0

%files         -n gem-google-apis-pubsublite-v1-devel

%files         -n gem-google-apis-safebrowsing-v4
%ruby_gemspecdir/google-apis-safebrowsing_v4-0.14.0.gemspec
%ruby_gemslibdir/google-apis-safebrowsing_v4-0.14.0

%files         -n gem-google-apis-safebrowsing-v4-doc
%ruby_gemsdocdir/google-apis-safebrowsing_v4-0.14.0

%files         -n gem-google-apis-safebrowsing-v4-devel

%files         -n gem-google-apis-script-v1
%ruby_gemspecdir/google-apis-script_v1-0.17.0.gemspec
%ruby_gemslibdir/google-apis-script_v1-0.17.0

%files         -n gem-google-apis-script-v1-doc
%ruby_gemsdocdir/google-apis-script_v1-0.17.0

%files         -n gem-google-apis-script-v1-devel

%files         -n gem-google-apis-searchconsole-v1
%ruby_gemspecdir/google-apis-searchconsole_v1-0.13.0.gemspec
%ruby_gemslibdir/google-apis-searchconsole_v1-0.13.0

%files         -n gem-google-apis-searchconsole-v1-doc
%ruby_gemsdocdir/google-apis-searchconsole_v1-0.13.0

%files         -n gem-google-apis-searchconsole-v1-devel

%files         -n gem-google-apis-secretmanager-v1
%ruby_gemspecdir/google-apis-secretmanager_v1-0.30.0.gemspec
%ruby_gemslibdir/google-apis-secretmanager_v1-0.30.0

%files         -n gem-google-apis-secretmanager-v1-doc
%ruby_gemsdocdir/google-apis-secretmanager_v1-0.30.0

%files         -n gem-google-apis-secretmanager-v1-devel

%files         -n gem-google-apis-securitycenter-v1
%ruby_gemspecdir/google-apis-securitycenter_v1-0.44.0.gemspec
%ruby_gemslibdir/google-apis-securitycenter_v1-0.44.0

%files         -n gem-google-apis-securitycenter-v1-doc
%ruby_gemsdocdir/google-apis-securitycenter_v1-0.44.0

%files         -n gem-google-apis-securitycenter-v1-devel

%files         -n gem-google-apis-serviceconsumermanagement-v1
%ruby_gemspecdir/google-apis-serviceconsumermanagement_v1-0.27.0.gemspec
%ruby_gemslibdir/google-apis-serviceconsumermanagement_v1-0.27.0

%files         -n gem-google-apis-serviceconsumermanagement-v1-doc
%ruby_gemsdocdir/google-apis-serviceconsumermanagement_v1-0.27.0

%files         -n gem-google-apis-serviceconsumermanagement-v1-devel

%files         -n gem-google-apis-servicecontrol-v1
%ruby_gemspecdir/google-apis-servicecontrol_v1-0.25.0.gemspec
%ruby_gemslibdir/google-apis-servicecontrol_v1-0.25.0

%files         -n gem-google-apis-servicecontrol-v1-doc
%ruby_gemsdocdir/google-apis-servicecontrol_v1-0.25.0

%files         -n gem-google-apis-servicecontrol-v1-devel

%files         -n gem-google-apis-servicecontrol-v2
%ruby_gemspecdir/google-apis-servicecontrol_v2-0.24.0.gemspec
%ruby_gemslibdir/google-apis-servicecontrol_v2-0.24.0

%files         -n gem-google-apis-servicecontrol-v2-doc
%ruby_gemsdocdir/google-apis-servicecontrol_v2-0.24.0

%files         -n gem-google-apis-servicecontrol-v2-devel

%files         -n gem-google-apis-servicedirectory-v1
%ruby_gemspecdir/google-apis-servicedirectory_v1-0.24.0.gemspec
%ruby_gemslibdir/google-apis-servicedirectory_v1-0.24.0

%files         -n gem-google-apis-servicedirectory-v1-doc
%ruby_gemsdocdir/google-apis-servicedirectory_v1-0.24.0

%files         -n gem-google-apis-servicedirectory-v1-devel

%files         -n gem-google-apis-servicemanagement-v1
%ruby_gemspecdir/google-apis-servicemanagement_v1-0.35.0.gemspec
%ruby_gemslibdir/google-apis-servicemanagement_v1-0.35.0

%files         -n gem-google-apis-servicemanagement-v1-doc
%ruby_gemsdocdir/google-apis-servicemanagement_v1-0.35.0

%files         -n gem-google-apis-servicemanagement-v1-devel

%files         -n gem-google-apis-servicenetworking-v1
%ruby_gemspecdir/google-apis-servicenetworking_v1-0.33.0.gemspec
%ruby_gemslibdir/google-apis-servicenetworking_v1-0.33.0

%files         -n gem-google-apis-servicenetworking-v1-doc
%ruby_gemsdocdir/google-apis-servicenetworking_v1-0.33.0

%files         -n gem-google-apis-servicenetworking-v1-devel

%files         -n gem-google-apis-servicenetworking-v1beta
%ruby_gemspecdir/google-apis-servicenetworking_v1beta-0.29.0.gemspec
%ruby_gemslibdir/google-apis-servicenetworking_v1beta-0.29.0

%files         -n gem-google-apis-servicenetworking-v1beta-doc
%ruby_gemsdocdir/google-apis-servicenetworking_v1beta-0.29.0

%files         -n gem-google-apis-servicenetworking-v1beta-devel

%files         -n gem-google-apis-serviceusage-v1
%ruby_gemspecdir/google-apis-serviceusage_v1-0.26.0.gemspec
%ruby_gemslibdir/google-apis-serviceusage_v1-0.26.0

%files         -n gem-google-apis-serviceusage-v1-doc
%ruby_gemsdocdir/google-apis-serviceusage_v1-0.26.0

%files         -n gem-google-apis-serviceusage-v1-devel

%files         -n gem-google-apis-sheets-v4
%ruby_gemspecdir/google-apis-sheets_v4-0.19.0.gemspec
%ruby_gemslibdir/google-apis-sheets_v4-0.19.0

%files         -n gem-google-apis-sheets-v4-doc
%ruby_gemsdocdir/google-apis-sheets_v4-0.19.0

%files         -n gem-google-apis-sheets-v4-devel

%files         -n gem-google-apis-site-verification-v1
%ruby_gemspecdir/google-apis-site_verification_v1-0.11.0.gemspec
%ruby_gemslibdir/google-apis-site_verification_v1-0.11.0

%files         -n gem-google-apis-site-verification-v1-doc
%ruby_gemsdocdir/google-apis-site_verification_v1-0.11.0

%files         -n gem-google-apis-site-verification-v1-devel

%files         -n gem-google-apis-slides-v1
%ruby_gemspecdir/google-apis-slides_v1-0.20.0.gemspec
%ruby_gemslibdir/google-apis-slides_v1-0.20.0

%files         -n gem-google-apis-slides-v1-doc
%ruby_gemsdocdir/google-apis-slides_v1-0.20.0

%files         -n gem-google-apis-slides-v1-devel

%files         -n gem-google-apis-smartdevicemanagement-v1
%ruby_gemspecdir/google-apis-smartdevicemanagement_v1-0.15.0.gemspec
%ruby_gemslibdir/google-apis-smartdevicemanagement_v1-0.15.0

%files         -n gem-google-apis-smartdevicemanagement-v1-doc
%ruby_gemsdocdir/google-apis-smartdevicemanagement_v1-0.15.0

%files         -n gem-google-apis-smartdevicemanagement-v1-devel

%files         -n gem-google-apis-sourcerepo-v1
%ruby_gemspecdir/google-apis-sourcerepo_v1-0.18.0.gemspec
%ruby_gemslibdir/google-apis-sourcerepo_v1-0.18.0

%files         -n gem-google-apis-sourcerepo-v1-doc
%ruby_gemsdocdir/google-apis-sourcerepo_v1-0.18.0

%files         -n gem-google-apis-sourcerepo-v1-devel

%files         -n gem-google-apis-spanner-v1
%ruby_gemspecdir/google-apis-spanner_v1-0.37.0.gemspec
%ruby_gemslibdir/google-apis-spanner_v1-0.37.0

%files         -n gem-google-apis-spanner-v1-doc
%ruby_gemsdocdir/google-apis-spanner_v1-0.37.0

%files         -n gem-google-apis-spanner-v1-devel

%files         -n gem-google-apis-speech-v1
%ruby_gemspecdir/google-apis-speech_v1-0.26.0.gemspec
%ruby_gemslibdir/google-apis-speech_v1-0.26.0

%files         -n gem-google-apis-speech-v1-doc
%ruby_gemsdocdir/google-apis-speech_v1-0.26.0

%files         -n gem-google-apis-speech-v1-devel

%files         -n gem-google-apis-sqladmin-v1
%ruby_gemspecdir/google-apis-sqladmin_v1-0.27.0.gemspec
%ruby_gemslibdir/google-apis-sqladmin_v1-0.27.0

%files         -n gem-google-apis-sqladmin-v1-doc
%ruby_gemsdocdir/google-apis-sqladmin_v1-0.27.0

%files         -n gem-google-apis-sqladmin-v1-devel

%files         -n gem-google-apis-sqladmin-v1beta4
%ruby_gemspecdir/google-apis-sqladmin_v1beta4-0.38.0.gemspec
%ruby_gemslibdir/google-apis-sqladmin_v1beta4-0.38.0

%files         -n gem-google-apis-sqladmin-v1beta4-doc
%ruby_gemsdocdir/google-apis-sqladmin_v1beta4-0.38.0

%files         -n gem-google-apis-sqladmin-v1beta4-devel

%files         -n gem-google-apis-storage-v1
%ruby_gemspecdir/google-apis-storage_v1-0.19.0.gemspec
%ruby_gemslibdir/google-apis-storage_v1-0.19.0

%files         -n gem-google-apis-storage-v1-doc
%ruby_gemsdocdir/google-apis-storage_v1-0.19.0

%files         -n gem-google-apis-storage-v1-devel

%files         -n gem-google-apis-storagetransfer-v1
%ruby_gemspecdir/google-apis-storagetransfer_v1-0.34.0.gemspec
%ruby_gemslibdir/google-apis-storagetransfer_v1-0.34.0

%files         -n gem-google-apis-storagetransfer-v1-doc
%ruby_gemsdocdir/google-apis-storagetransfer_v1-0.34.0

%files         -n gem-google-apis-storagetransfer-v1-devel

%files         -n gem-google-apis-streetviewpublish-v1
%ruby_gemspecdir/google-apis-streetviewpublish_v1-0.23.0.gemspec
%ruby_gemslibdir/google-apis-streetviewpublish_v1-0.23.0

%files         -n gem-google-apis-streetviewpublish-v1-doc
%ruby_gemsdocdir/google-apis-streetviewpublish_v1-0.23.0

%files         -n gem-google-apis-streetviewpublish-v1-devel

%files         -n gem-google-apis-sts-v1
%ruby_gemspecdir/google-apis-sts_v1-0.24.0.gemspec
%ruby_gemslibdir/google-apis-sts_v1-0.24.0

%files         -n gem-google-apis-sts-v1-doc
%ruby_gemsdocdir/google-apis-sts_v1-0.24.0

%files         -n gem-google-apis-sts-v1-devel

%files         -n gem-google-apis-sts-v1beta
%ruby_gemspecdir/google-apis-sts_v1beta-0.20.0.gemspec
%ruby_gemslibdir/google-apis-sts_v1beta-0.20.0

%files         -n gem-google-apis-sts-v1beta-doc
%ruby_gemsdocdir/google-apis-sts_v1beta-0.20.0

%files         -n gem-google-apis-sts-v1beta-devel

%files         -n gem-google-api-client
%ruby_gemspecdir/google-api-client-0.53.0.gemspec
%ruby_gemslibdir/google-api-client-0.53.0

%files         -n gem-google-api-client-doc
# %ruby_gemsdocdir/google-api-client-0.53.0

%files         -n gem-google-api-client-devel

%files         -n gem-google-apis-core
%ruby_gemspecdir/google-apis-core-0.9.0.gemspec
%ruby_gemslibdir/google-apis-core-0.9.0

%files         -n gem-google-apis-core-doc
%ruby_gemsdocdir/google-apis-core-0.9.0

%files         -n gem-google-apis-core-devel

%files         -n gem-google-apis-generator
%ruby_gemspecdir/google-apis-generator-0.10.0.gemspec
%ruby_gemslibdir/google-apis-generator-0.10.0

%files         -n generate-api
%_bindir/generate-api

%files         -n gem-google-apis-generator-doc
%ruby_gemsdocdir/google-apis-generator-0.10.0

%files         -n gem-google-apis-generator-devel


%changelog
* Sat Feb 04 2023 Pavel Skrylev <majioa@altlinux.org> 20221017-alt1.1
- ! fixed dep to redis

* Mon Oct 17 2022 Pavel Skrylev <majioa@altlinux.org> 20221017-alt1
- ^ 20210602-alt1 -> 20221017-alt1

* Wed Jun 02 2021 Pavel Skrylev <majioa@altlinux.org> 20210602-alt1
- + strictly trimmed packaged gem with Ruby Policy 2.0

Name:          google-api-ruby-client
Version:       20210602
Release:       alt1
Summary:       REST client for Google APIs
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/googleapis/google-api-ruby-client
Vcs:           https://github.com/googleapis/google-api-ruby-client.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(activesupport) >= 5.0
BuildRequires: gem(gems) >= 1.2 gem(gems) < 2
BuildRequires: gem(thor) >= 0.20 gem(thor) < 2.0
BuildRequires: gem(representable) >= 3.0 gem(representable) < 4
BuildRequires: gem(retriable) >= 2.0 gem(retriable) < 4.0
BuildRequires: gem(addressable) >= 2.5.1 gem(addressable) < 3
BuildRequires: gem(mini_mime) >= 1.0 gem(mini_mime) < 2
BuildRequires: gem(signet) >= 0.14 gem(signet) < 1
BuildRequires: gem(googleauth) >= 0.14 gem(googleauth) < 1
BuildRequires: gem(httpclient) >= 2.8.1 gem(httpclient) < 3.0
BuildRequires: gem(rexml) >= 0
BuildRequires: gem(webrick) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names web,cli,/beta,/alpha,/apis-[aefhj-rt-z],/apis-g[a-df-z],/apis-d[a-hj-mo-z],/apis-c[a-kmnp-z],/genomics,/dia,/dig,/display,/apis-cloud[a-ps-z],/classroom,/apis-cloudr.*v[23],/apis-co[a-ps-z],google-api-ruby-client

%description
This repository contains a set of simple client libraries for various Google
APIs. These libraries are generated automatically from Discovery Documents,
and the code generator is also hosted here in this repository.

Each client provides:

* A client object that connects to the HTTP/JSON REST endpoint for the service.
* Ruby objects for data structures related to the service.
* Integration with the googleauth gem for authentication using OAuth, API keys,
  and service accounts.
* Control of retry, pagination, and timeouts.

These client libraries are officially supported by Google, and are updated
regularly to track changes to the service. However, many Google services,
especially Google Cloud Platform services such as Cloud Storage, Pub/Sub,
and BigQuery, may provide a more modern client that is easier to use and more
performant. See the section below titled "Which client should I use?" for more
information.


%package       -n gem-google-apis-discovery-v1
Version:       0.4.0
Release:       alt1
Summary:       Simple REST client for API Discovery Service V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.1 gem(google-apis-core) < 1
Provides:      gem(google-apis-discovery_v1) = 0.4.0

%description   -n gem-google-apis-discovery-v1
This is the simple REST client for API Discovery Service V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the API Discovery Service, but note that some
services may provide a separate modern client that is easier to use.


%package       -n gem-google-apis-discovery-v1-doc
Version:       0.4.0
Release:       alt1
Summary:       Simple REST client for API Discovery Service V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-discovery_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-discovery_v1) = 0.4.0

%description   -n gem-google-apis-discovery-v1-doc
Simple REST client for API Discovery Service V1 documentation files.

This is the simple REST client for API Discovery Service V1. Simple REST clients
are Ruby client libraries that provide access to Google services via their HTTP
REST API endpoints. These libraries are generated and updated automatically
based on the discovery documents published by the service, and they handle most
concerns such as authentication, pagination, retry, timeouts, and logging. You
can use this client to access the API Discovery Service, but note that some
services may provide a separate modern client that is easier to use.

%description   -n gem-google-apis-discovery-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-discovery_v1.


%package       -n gem-google-apis-storage-v1
Version:       0.4.0
Release:       alt1
Summary:       Simple REST client for Cloud Storage JSON API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.1 gem(google-apis-core) < 1
Provides:      gem(google-apis-storage_v1) = 0.4.0

%description   -n gem-google-apis-storage-v1
This is the simple REST client for Cloud Storage JSON API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Cloud Storage JSON API, but
note that some services may provide a separate modern client that is easier to
use.


%package       -n gem-google-apis-storage-v1-doc
Version:       0.4.0
Release:       alt1
Summary:       Simple REST client for Cloud Storage JSON API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-storage_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-storage_v1) = 0.4.0

%description   -n gem-google-apis-storage-v1-doc
Simple REST client for Cloud Storage JSON API V1 documentation files.

This is the simple REST client for Cloud Storage JSON API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Cloud Storage JSON API, but
note that some services may provide a separate modern client that is easier to
use.

%description   -n gem-google-apis-storage-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-storage_v1.


%package       -n gem-google-apis-generator
Version:       0.3.0
Release:       alt1
Summary:       Code generator for legacy Google REST clients
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(activesupport) >= 5.0
Requires:      gem(gems) >= 1.2 gem(gems) < 2
Requires:      gem(google-apis-core) >= 0.1 gem(google-apis-core) < 1
Requires:      gem(google-apis-discovery_v1) >= 0.0 gem(google-apis-discovery_v1) < 1
Requires:      gem(thor) >= 0.20 gem(thor) < 2.0
Provides:      gem(google-apis-generator) = 0.3.0

%description   -n gem-google-apis-generator
Code generator for legacy Google REST clients.


%package       -n generate-api
Version:       0.3.0
Release:       alt1
Summary:       Code generator for legacy Google REST clients executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета google-apis-generator
Group:         Other
BuildArch:     noarch

Requires:      gem(google-apis-generator) = 0.3.0

%description   -n generate-api
Code generator for legacy Google REST clients executable(s).

%description   -n generate-api -l ru_RU.UTF-8
Исполнямка для самоцвета google-apis-generator.


%package       -n gem-google-apis-generator-doc
Version:       0.3.0
Release:       alt1
Summary:       Code generator for legacy Google REST clients documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-generator
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-generator) = 0.3.0

%description   -n gem-google-apis-generator-doc
Code generator for legacy Google REST clients documentation files.

%description   -n gem-google-apis-generator-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-generator.


%package       -n gem-google-apis-iamcredentials-v1
Version:       0.4.0
Release:       alt1
Summary:       Simple REST client for IAM Service Account Credentials API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.1 gem(google-apis-core) < 1
Provides:      gem(google-apis-iamcredentials_v1) = 0.4.0

%description   -n gem-google-apis-iamcredentials-v1
This is the simple REST client for IAM Service Account Credentials API V1.
Simple REST clients are Ruby client libraries that provide access to Google
services via their HTTP REST API endpoints. These libraries are generated and
updated automatically based on the discovery documents published by the service,
and they handle most concerns such as authentication, pagination, retry,
timeouts, and logging. You can use this client to access the IAM Service Account
Credentials API, but note that some services may provide a separate modern
client that is easier to use.


%package       -n gem-google-apis-iamcredentials-v1-doc
Version:       0.4.0
Release:       alt1
Summary:       Simple REST client for IAM Service Account Credentials API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-iamcredentials_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-iamcredentials_v1) = 0.4.0

%description   -n gem-google-apis-iamcredentials-v1-doc
Simple REST client for IAM Service Account Credentials API V1 documentation
files.

This is the simple REST client for IAM Service Account Credentials API V1.
Simple REST clients are Ruby client libraries that provide access to Google
services via their HTTP REST API endpoints. These libraries are generated and
updated automatically based on the discovery documents published by the service,
and they handle most concerns such as authentication, pagination, retry,
timeouts, and logging. You can use this client to access the IAM Service Account
Credentials API, but note that some services may provide a separate modern
client that is easier to use.

%description   -n gem-google-apis-iamcredentials-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-iamcredentials_v1.


%package       -n gem-google-apis-dns-v1
Version:       0.10.0
Release:       alt1
Summary:       Simple REST client for Cloud DNS API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.1 gem(google-apis-core) < 1
Provides:      gem(google-apis-dns_v1) = 0.10.0

%description   -n gem-google-apis-dns-v1
This is the simple REST client for Cloud DNS API V1. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Cloud DNS API, but note that some services may provide
a separate modern client that is easier to use.


%package       -n gem-google-apis-dns-v1-doc
Version:       0.10.0
Release:       alt1
Summary:       Simple REST client for Cloud DNS API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-dns_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-dns_v1) = 0.10.0

%description   -n gem-google-apis-dns-v1-doc
Simple REST client for Cloud DNS API V1 documentation files.

This is the simple REST client for Cloud DNS API V1. Simple REST clients are
Ruby client libraries that provide access to Google services via their HTTP REST
API endpoints. These libraries are generated and updated automatically based on
the discovery documents published by the service, and they handle most concerns
such as authentication, pagination, retry, timeouts, and logging. You can use
this client to access the Cloud DNS API, but note that some services may provide
a separate modern client that is easier to use.

%description   -n gem-google-apis-dns-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-dns_v1.


%package       -n gem-google-apis-cloudresourcemanager-v1
Version:       0.10.0
Release:       alt1
Summary:       Simple REST client for Cloud Resource Manager API V1
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.1 gem(google-apis-core) < 1
Provides:      gem(google-apis-cloudresourcemanager_v1) = 0.10.0

%description   -n gem-google-apis-cloudresourcemanager-v1
This is the simple REST client for Cloud Resource Manager API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Cloud Resource Manager API,
but note that some services may provide a separate modern client that is easier
to use.


%package       -n gem-google-apis-cloudresourcemanager-v1-doc
Version:       0.10.0
Release:       alt1
Summary:       Simple REST client for Cloud Resource Manager API V1 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-cloudresourcemanager_v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-cloudresourcemanager_v1) = 0.10.0

%description   -n gem-google-apis-cloudresourcemanager-v1-doc
Simple REST client for Cloud Resource Manager API V1 documentation files.

This is the simple REST client for Cloud Resource Manager API V1. Simple REST
clients are Ruby client libraries that provide access to Google services via
their HTTP REST API endpoints. These libraries are generated and updated
automatically based on the discovery documents published by the service, and
they handle most concerns such as authentication, pagination, retry, timeouts,
and logging. You can use this client to access the Cloud Resource Manager API,
but note that some services may provide a separate modern client that is easier
to use.

%description   -n gem-google-apis-cloudresourcemanager-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-cloudresourcemanager_v1.


%package       -n gem-google-apis-bigquery-v2
Version:       0.12.0
Release:       alt1
Summary:       Simple REST client for BigQuery API V2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.1 gem(google-apis-core) < 1
Provides:      gem(google-apis-bigquery_v2) = 0.12.0

%description   -n gem-google-apis-bigquery-v2
This is the simple REST client for BigQuery API V2. Simple REST clients are Ruby
client libraries that provide access to Google services via their HTTP REST API
endpoints. These libraries are generated and updated automatically based on the
discovery documents published by the service, and they handle most concerns such
as authentication, pagination, retry, timeouts, and logging. You can use this
client to access the BigQuery API, but note that some services may provide a
separate modern client that is easier to use.


%package       -n gem-google-apis-bigquery-v2-doc
Version:       0.12.0
Release:       alt1
Summary:       Simple REST client for BigQuery API V2 documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-bigquery_v2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-bigquery_v2) = 0.12.0

%description   -n gem-google-apis-bigquery-v2-doc
Simple REST client for BigQuery API V2 documentation files.

This is the simple REST client for BigQuery API V2. Simple REST clients are Ruby
client libraries that provide access to Google services via their HTTP REST API
endpoints. These libraries are generated and updated automatically based on the
discovery documents published by the service, and they handle most concerns such
as authentication, pagination, retry, timeouts, and logging. You can use this
client to access the BigQuery API, but note that some services may provide a
separate modern client that is easier to use.

%description   -n gem-google-apis-bigquery-v2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-bigquery_v2.


%package       -n gem-google-apis-core
Version:       0.3.0
Release:       alt1
Summary:       Common utility and base classes for legacy Google REST clients
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(representable) >= 3.0 gem(representable) < 4
Requires:      gem(retriable) >= 2.0 gem(retriable) < 4.0
Requires:      gem(addressable) >= 2.5.1 gem(addressable) < 3
Requires:      gem(mini_mime) >= 1.0 gem(mini_mime) < 2
Requires:      gem(signet) >= 0.14 gem(signet) < 1
Requires:      gem(googleauth) >= 0.14 gem(googleauth) < 1
Requires:      gem(httpclient) >= 2.8.1 gem(httpclient) < 3.0
Requires:      gem(rexml) >= 0
Requires:      gem(webrick) >= 0
Provides:      gem(google-apis-core) = 0.3.0

%description   -n gem-google-apis-core
Common utility and base classes for legacy Google REST clients.

%package       -n gem-google-apis-core-doc
Version:       0.3.0
Release:       alt1
Summary:       Common utility and base classes for legacy Google REST clients documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-apis-core
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-apis-core) = 0.3.0

%description   -n gem-google-apis-core-doc
Common utility and base classes for legacy Google REST clients documentation
files.

%description   -n gem-google-apis-core-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-apis-core.


%package       -n gem-google-api-client
Version:       0.53.0
Release:       alt1
Summary:       Client for accessing Google APIs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-apis-core) >= 0.1 gem(google-apis-core) < 1
Requires:      gem(google-apis-generator) >= 0.1 gem(google-apis-generator) < 1
Provides:      gem(google-api-client) = 0.53.0
Provides:      ruby-google-api = %EVR
Obsoletes:     ruby-google-api < %EVR

%description   -n gem-google-api-client
Client for accessing Google APIs.


%package       -n gem-google-api-client-doc
Version:       0.53.0
Release:       alt1
Summary:       Client for accessing Google APIs documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-api-client
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-api-client) = 0.53.0

%description   -n gem-google-api-client-doc
Client for accessing Google APIs documentation files.

%description   -n gem-google-api-client-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-api-client.


%prep
%setup

%build
%ruby_build

%install
%ruby_install
rm -rf %buildroot%ruby_gemsdocdir/google-api-client-*

%check
%ruby_test

%files

%files         -n gem-google-apis-discovery-v1
%ruby_gemspecdir/google-apis-discovery_v1-0.4.0.gemspec
%ruby_gemslibdir/google-apis-discovery_v1-0.4.0

%files         -n gem-google-apis-discovery-v1-doc
%ruby_gemsdocdir/google-apis-discovery_v1-0.4.0

%files         -n gem-google-apis-storage-v1
%ruby_gemspecdir/google-apis-storage_v1-0.4.0.gemspec
%ruby_gemslibdir/google-apis-storage_v1-0.4.0

%files         -n gem-google-apis-storage-v1-doc
%ruby_gemsdocdir/google-apis-storage_v1-0.4.0

%files         -n gem-google-apis-generator
%ruby_gemspecdir/google-apis-generator-0.3.0.gemspec
%ruby_gemslibdir/google-apis-generator-0.3.0

%files         -n generate-api
%_bindir/generate-api

%files         -n gem-google-apis-generator-doc
%ruby_gemsdocdir/google-apis-generator-0.3.0

%files         -n gem-google-apis-iamcredentials-v1
%ruby_gemspecdir/google-apis-iamcredentials_v1-0.4.0.gemspec
%ruby_gemslibdir/google-apis-iamcredentials_v1-0.4.0

%files         -n gem-google-apis-iamcredentials-v1-doc
%ruby_gemsdocdir/google-apis-iamcredentials_v1-0.4.0

%files         -n gem-google-apis-dns-v1
%ruby_gemspecdir/google-apis-dns_v1-0.10.0.gemspec
%ruby_gemslibdir/google-apis-dns_v1-0.10.0

%files         -n gem-google-apis-dns-v1-doc
%ruby_gemsdocdir/google-apis-dns_v1-0.10.0

%files         -n gem-google-apis-cloudresourcemanager-v1
%ruby_gemspecdir/google-apis-cloudresourcemanager_v1-0.10.0.gemspec
%ruby_gemslibdir/google-apis-cloudresourcemanager_v1-0.10.0

%files         -n gem-google-apis-cloudresourcemanager-v1-doc
%ruby_gemsdocdir/google-apis-cloudresourcemanager_v1-0.10.0

%files         -n gem-google-apis-bigquery-v2
%ruby_gemspecdir/google-apis-bigquery_v2-0.12.0.gemspec
%ruby_gemslibdir/google-apis-bigquery_v2-0.12.0

%files         -n gem-google-apis-bigquery-v2-doc
%ruby_gemsdocdir/google-apis-bigquery_v2-0.12.0

%files         -n gem-google-apis-core
%ruby_gemspecdir/google-apis-core-0.3.0.gemspec
%ruby_gemslibdir/google-apis-core-0.3.0

%files         -n gem-google-apis-core-doc
%ruby_gemsdocdir/google-apis-core-0.3.0

%files         -n gem-google-api-client
%ruby_gemspecdir/google-api-client-0.53.0.gemspec
%ruby_gemslibdir/google-api-client-0.53.0

%files         -n gem-google-api-client-doc
# %ruby_gemsdocdir/google-api-client-0.53.0


%changelog
* Wed Jun 02 2021 Pavel Skrylev <majioa@altlinux.org> 20210602-alt1
- + strictly trimmed packaged gem with Ruby Policy 2.0

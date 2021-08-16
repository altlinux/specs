Name:          google-cloud-ruby
Version:       20210531
Release:       alt1
Summary:       Google Cloud Client Library for Ruby
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/googleapis/google-cloud-ruby
Vcs:           https://github.com/googleapis/google-cloud-ruby.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
Patch:         version.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(minitest) >= 5.14 gem(minitest) < 6
BuildRequires: gem(rake) >= 12.0 gem(rake) < 14
BuildRequires: gem(simplecov) >= 0.17 gem(simplecov) < 1
BuildRequires: gem(grpc-google-iam-v1) >= 0.6.10 gem(grpc-google-iam-v1) < 2.0
BuildRequires: gem(rbtree) >= 0.4.2 gem(rbtree) < 0.5
BuildRequires: gem(faraday) >= 0.17.3 gem(faraday) < 2.0
BuildRequires: gem(googleapis-common-protos) >= 1.3.10 gem(googleapis-common-protos) < 2.0
BuildRequires: gem(googleapis-common-protos-types) >= 1.0.5 gem(googleapis-common-protos-types) < 2.0
BuildRequires: gem(googleauth) >= 0.12 gem(googleauth) < 1
BuildRequires: gem(google-apis-cloudresourcemanager_v1) >= 0.1 gem(google-apis-cloudresourcemanager_v1) < 1
BuildRequires: gem(google-gax) >= 1.8 gem(google-gax) < 2
BuildRequires: gem(concurrent-ruby) >= 1.1 gem(concurrent-ruby) < 2
#BuildRequires: gem(google-apis-iamcredentials_v1) >= 0.1 gem(google-apis-iamcredentials_v1) < 1
#BuildRequires: gem(google-apis-storage_v1) >= 0.1 gem(google-apis-storage_v1) < 1
BuildRequires: gem(digest-crc) >= 0.4 gem(digest-crc) < 1
BuildRequires: gem(addressable) >= 2.5 gem(addressable) < 3
BuildRequires: gem(mini_mime) >= 1.0 gem(mini_mime) < 2
#BuildRequires: gem(google-apis-bigquery_v2) >= 0.1 gem(google-apis-bigquery_v2) < 1
BuildRequires: gem(binding_of_caller) >= 0.7 gem(binding_of_caller) < 2
BuildRequires: gem(zonefile) >= 1.04 gem(zonefile) < 2
#BuildRequires: gem(gapic-common) >= 0.4.1 gem(gapic-common) < 1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency binding_of_caller >= 0.7,binding_of_caller < 2
%ruby_ignore_names samples,snippets,simple-app,sinatra2-app,rails4-app,rails5-app,simple_app

%description
Idiomatic Ruby client for Google Cloud Platform services.


%package       -n gem-google-cloud-channel-v1
Version:       0.6.0
Release:       alt1
Summary:       API Client library for the Cloud Channel V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-channel-v1) = 0.6.0

%description   -n gem-google-cloud-channel-v1
You can use Channel Services to manage your relationships with your partners and
your customers. Channel Services include a console and APIs to view and
provision links between distributors and resellers, customers and entitlements.
Note that google-cloud-channel-v1 is a version-specific client library. For most
uses, we recommend installing the main client library google-cloud-channel
instead. See the readme for more details.


%package       -n gem-google-cloud-channel-v1-doc
Version:       0.6.0
Release:       alt1
Summary:       API Client library for the Cloud Channel V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-channel-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-channel-v1) = 0.6.0

%description   -n gem-google-cloud-channel-v1-doc
API Client library for the Cloud Channel V1 API documentation files.

You can use Channel Services to manage your relationships with your partners and
your customers. Channel Services include a console and APIs to view and
provision links between distributors and resellers, customers and entitlements.
Note that google-cloud-channel-v1 is a version-specific client library. For most
uses, we recommend installing the main client library google-cloud-channel
instead. See the readme for more details.

%description   -n gem-google-cloud-channel-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-channel-v1.


%package       -n gem-google-cloud-bigquery-data-transfer-v1
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the BigQuery Data Transfer Service V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-bigquery-data_transfer-v1) = 0.4.0

%description   -n gem-google-cloud-bigquery-data-transfer-v1
Schedules queries and transfers external data from SaaS applications to Google
BigQuery on a regular basis. Note that google-cloud-bigquery-data_transfer-v1 is
a version-specific client library. For most uses, we recommend installing the
main client library google-cloud-bigquery-data_transfer instead. See the readme
for more details.


%package       -n gem-google-cloud-bigquery-data-transfer-v1-doc
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the BigQuery Data Transfer Service V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-bigquery-data_transfer-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-bigquery-data_transfer-v1) = 0.4.0

%description   -n gem-google-cloud-bigquery-data-transfer-v1-doc
API Client library for the BigQuery Data Transfer Service V1 API documentation
files.

Schedules queries and transfers external data from SaaS applications to Google
BigQuery on a regular basis. Note that google-cloud-bigquery-data_transfer-v1 is
a version-specific client library. For most uses, we recommend installing the
main client library google-cloud-bigquery-data_transfer instead. See the readme
for more details.

%description   -n gem-google-cloud-bigquery-data-transfer-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-bigquery-data_transfer-v1.


%package       -n gem-google-cloud-core
Version:       1.6.0
Release:       alt1
Summary:       Internal shared library for google-cloud-ruby
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-env) >= 1.0 gem(google-cloud-env) < 2
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-core) = 1.6.0

%description   -n gem-google-cloud-core
google-cloud-core is the internal shared library for google-cloud-ruby.


%package       -n gem-google-cloud-core-doc
Version:       1.6.0
Release:       alt1
Summary:       Internal shared library for google-cloud-ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-core
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-core) = 1.6.0

%description   -n gem-google-cloud-core-doc
Internal shared library for google-cloud-ruby documentation
files.

google-cloud-core is the internal shared library for google-cloud-ruby.

%description   -n gem-google-cloud-core-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-core.


%package       -n gem-google-cloud-workflows-v1beta
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Workflows V1beta API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-workflows-v1beta) = 0.3.0

%description   -n gem-google-cloud-workflows-v1beta
Workflows link series of serverless tasks together in an order you define.
Combine the power of Google Cloud's APIs, serverless products like Cloud
Functions and Cloud Run, and calls to external APIs to create flexible
serverless applications. Workflows requires no infrastructure management and
scales seamlessly with demand, including scaling down to zero.. Note that
google-cloud-workflows-v1beta is a version-specific client library. For most
uses, we recommend installing the main client library google-cloud-workflows
instead. See the readme for more details.


%package       -n gem-google-cloud-workflows-v1beta-doc
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Workflows V1beta API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-workflows-v1beta
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-workflows-v1beta) = 0.3.0

%description   -n gem-google-cloud-workflows-v1beta-doc
API Client library for the Workflows V1beta API documentation files.

Workflows link series of serverless tasks together in an order you define.
Combine the power of Google Cloud's APIs, serverless products like Cloud
Functions and Cloud Run, and calls to external APIs to create flexible
serverless applications. Workflows requires no infrastructure management and
scales seamlessly with demand, including scaling down to zero.. Note that
google-cloud-workflows-v1beta is a version-specific client library. For most
uses, we recommend installing the main client library google-cloud-workflows
instead. See the readme for more details.

%description   -n gem-google-cloud-workflows-v1beta-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-workflows-v1beta.


%package       -n gem-google-cloud-scheduler-v1beta1
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud Scheduler V1beta1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-scheduler-v1beta1) = 0.4.0

%description   -n gem-google-cloud-scheduler-v1beta1
Cloud Scheduler is a fully managed enterprise-grade cron job scheduler. It
allows you to schedule virtually any job, including batch, big data jobs, cloud
infrastructure operations, and more. You can automate everything, including
retries in case of failure to reduce manual toil and intervention. Cloud
Scheduler even acts as a single pane of glass, allowing you to manage all your
automation tasks from one place. Note that google-cloud-scheduler-v1beta1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-scheduler instead. See the readme for more details.


%package       -n gem-google-cloud-scheduler-v1beta1-doc
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud Scheduler V1beta1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-scheduler-v1beta1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-scheduler-v1beta1) = 0.4.0

%description   -n gem-google-cloud-scheduler-v1beta1-doc
API Client library for the Cloud Scheduler V1beta1 API documentation
files.

Cloud Scheduler is a fully managed enterprise-grade cron job scheduler. It
allows you to schedule virtually any job, including batch, big data jobs, cloud
infrastructure operations, and more. You can automate everything, including
retries in case of failure to reduce manual toil and intervention. Cloud
Scheduler even acts as a single pane of glass, allowing you to manage all your
automation tasks from one place. Note that google-cloud-scheduler-v1beta1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-scheduler instead. See the readme for more details.

%description   -n gem-google-cloud-scheduler-v1beta1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-scheduler-v1beta1.


%package       -n gem-google-cloud-bigquery-connection-v1
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the BigQuery Connection V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Requires:      gem(grpc-google-iam-v1) >= 0.6.10 gem(grpc-google-iam-v1) < 2.0
Provides:      gem(google-cloud-bigquery-connection-v1) = 0.4.0

%description   -n gem-google-cloud-bigquery-connection-v1
The BigQuery Connection API allows users to manage BigQuery connections to
external data sources. Note that google-cloud-bigquery-connection-v1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-bigquery-connection instead. See the readme for more
details.


%package       -n gem-google-cloud-bigquery-connection-v1-doc
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the BigQuery Connection V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-bigquery-connection-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-bigquery-connection-v1) = 0.4.0

%description   -n gem-google-cloud-bigquery-connection-v1-doc
API Client library for the BigQuery Connection V1 API documentation files.

The BigQuery Connection API allows users to manage BigQuery connections to
external data sources. Note that google-cloud-bigquery-connection-v1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-bigquery-connection instead. See the readme for more
details.

%description   -n gem-google-cloud-bigquery-connection-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-bigquery-connection-v1.


%package       -n gem-google-cloud-tasks-v2beta3
Version:       0.6.0
Release:       alt1
Summary:       API Client library for the Cloud Tasks V2beta3 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Requires:      gem(grpc-google-iam-v1) >= 0.6.10 gem(grpc-google-iam-v1) < 2.0
Provides:      gem(google-cloud-tasks-v2beta3) = 0.6.0

%description   -n gem-google-cloud-tasks-v2beta3
Cloud Tasks is a fully managed service that allows you to manage the execution,
dispatch and delivery of a large number of distributed tasks. You can
asynchronously perform work outside of a user request. Your tasks can be
executed on App Engine or any arbitrary HTTP endpoint. Note that
google-cloud-tasks-v2beta3 is a version-specific client library. For most uses,
we recommend installing the main client library google-cloud-tasks instead. See
the readme for more details.


%package       -n gem-google-cloud-tasks-v2beta3-doc
Version:       0.6.0
Release:       alt1
Summary:       API Client library for the Cloud Tasks V2beta3 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-tasks-v2beta3
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-tasks-v2beta3) = 0.6.0

%description   -n gem-google-cloud-tasks-v2beta3-doc
API Client library for the Cloud Tasks V2beta3 API documentation files.

Cloud Tasks is a fully managed service that allows you to manage the execution,
dispatch and delivery of a large number of distributed tasks. You can
asynchronously perform work outside of a user request. Your tasks can be
executed on App Engine or any arbitrary HTTP endpoint. Note that
google-cloud-tasks-v2beta3 is a version-specific client library. For most uses,
we recommend installing the main client library google-cloud-tasks instead. See
the readme for more details.

%description   -n gem-google-cloud-tasks-v2beta3-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-tasks-v2beta3.


%package       -n gem-google-area120-tables-v1alpha1
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Area 120 Tables V1alpha1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-area120-tables-v1alpha1) = 0.2.0

%description   -n gem-google-area120-tables-v1alpha1
Using the Area 120 Tables API, you can query for tables, and
update/create/delete rows within tables programmatically. Note that
google-area120-tables-v1alpha1 is a version-specific client library. For most
uses, we recommend installing the main client library google-area120-tables
instead. See the readme for more details.


%package       -n gem-google-area120-tables-v1alpha1-doc
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Area 120 Tables V1alpha1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-area120-tables-v1alpha1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-area120-tables-v1alpha1) = 0.2.0

%description   -n gem-google-area120-tables-v1alpha1-doc
API Client library for the Area 120 Tables V1alpha1 API documentation
files.

Using the Area 120 Tables API, you can query for tables, and
update/create/delete rows within tables programmatically. Note that
google-area120-tables-v1alpha1 is a version-specific client library. For most
uses, we recommend installing the main client library google-area120-tables
instead. See the readme for more details.

%description   -n gem-google-area120-tables-v1alpha1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-area120-tables-v1alpha1.


%package       -n gem-google-cloud-speech
Version:       1.2.0
Release:       alt1
Summary:       API Client library for the Cloud Speech-to-Text API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-speech-v1) >= 0.0 gem(google-cloud-speech-v1) < 1
Requires:      gem(google-cloud-speech-v1p1beta1) >= 0.0 gem(google-cloud-speech-v1p1beta1) < 1
Provides:      gem(google-cloud-speech) = 1.2.0

%description   -n gem-google-cloud-speech
Google Speech-to-Text enables developers to convert audio to text by applying
powerful neural network models in an easy-to-use API. The API recognizes more
than 120 languages and variants to support your global user base. You can enable
voice command-and-control, transcribe audio from call centers, and more. It can
process real-time streaming or prerecorded audio, using Google's machine
learning technology.


%package       -n gem-google-cloud-speech-doc
Version:       1.2.0
Release:       alt1
Summary:       API Client library for the Cloud Speech-to-Text API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-speech
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-speech) = 1.2.0

%description   -n gem-google-cloud-speech-doc
API Client library for the Cloud Speech-to-Text API documentation files.

Google Speech-to-Text enables developers to convert audio to text by applying
powerful neural network models in an easy-to-use API. The API recognizes more
than 120 languages and variants to support your global user base. You can enable
voice command-and-control, transcribe audio from call centers, and more. It can
process real-time streaming or prerecorded audio, using Google's machine
learning technology.

%description   -n gem-google-cloud-speech-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-speech.


%package       -n gem-google-cloud-trace-v2
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Cloud Trace V2 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-trace-v2) = 0.3.0

%description   -n gem-google-cloud-trace-v2
The Cloud Trace API lets you send and retrieve latency data to and from Cloud
Trace. This API provides low-level interfaces for interacting directly with the
feature. For some languages, you can use OpenCensus, a set of open source
tracing and stats instrumentation libraries that work with multiple backends.
Note that google-cloud-trace-v2 is a version-specific client library. For most
uses, we recommend installing the main client library google-cloud-trace
instead. See the readme for more details.


%package       -n gem-google-cloud-trace-v2-doc
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Cloud Trace V2 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-trace-v2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-trace-v2) = 0.3.0

%description   -n gem-google-cloud-trace-v2-doc
API Client library for the Cloud Trace V2 API documentation files.

The Cloud Trace API lets you send and retrieve latency data to and from Cloud
Trace. This API provides low-level interfaces for interacting directly with the
feature. For some languages, you can use OpenCensus, a set of open source
tracing and stats instrumentation libraries that work with multiple backends.
Note that google-cloud-trace-v2 is a version-specific client library. For most
uses, we recommend installing the main client library google-cloud-trace
instead. See the readme for more details.

%description   -n gem-google-cloud-trace-v2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-trace-v2.


%package       -n gem-google-cloud-service-directory
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Service Directory API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-service_directory-v1) >= 0.1 gem(google-cloud-service_directory-v1) < 1
Requires:      gem(google-cloud-service_directory-v1beta1) >= 0.1 gem(google-cloud-service_directory-v1beta1) < 1
Provides:      gem(google-cloud-service_directory) = 1.1.0

%description   -n gem-google-cloud-service-directory
Service Directory is the single place to register, browse, and resolve
application services.


%package       -n gem-google-cloud-service-directory-doc
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Service Directory API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-service_directory
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-service_directory) = 1.1.0

%description   -n gem-google-cloud-service-directory-doc
API Client library for the Service Directory API documentation files.

Service Directory is the single place to register, browse, and resolve
application services.

%description   -n gem-google-cloud-service-directory-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-service_directory.


%package       -n gem-google-cloud-vision-v1
Version:       0.6.0
Release:       alt1
Summary:       API Client library for the Cloud Vision V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-vision-v1) = 0.6.0

%description   -n gem-google-cloud-vision-v1
Cloud Vision API allows developers to easily integrate vision detection features
within applications, including image labeling, face and landmark detection,
optical character recognition (OCR), and tagging of explicit content. Note that
google-cloud-vision-v1 is a version-specific client library. For most uses, we
recommend installing the main client library google-cloud-vision instead. See
the readme for more details.


%package       -n gem-google-cloud-vision-v1-doc
Version:       0.6.0
Release:       alt1
Summary:       API Client library for the Cloud Vision V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-vision-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-vision-v1) = 0.6.0

%description   -n gem-google-cloud-vision-v1-doc
API Client library for the Cloud Vision V1 API documentation files.

Cloud Vision API allows developers to easily integrate vision detection features
within applications, including image labeling, face and landmark detection,
optical character recognition (OCR), and tagging of explicit content. Note that
google-cloud-vision-v1 is a version-specific client library. For most uses, we
recommend installing the main client library google-cloud-vision instead. See
the readme for more details.

%description   -n gem-google-cloud-vision-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-vision-v1.


%package       -n gem-google-cloud-workflows-executions-v1beta
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Workflows Executions V1beta API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-workflows-executions-v1beta) = 0.3.0

%description   -n gem-google-cloud-workflows-executions-v1beta
Workflows link series of serverless tasks together in an order you define.
Combine the power of Google Cloud's APIs, serverless products like Cloud
Functions and Cloud Run, and calls to external APIs to create flexible
serverless applications. Workflows requires no infrastructure management and
scales seamlessly with demand, including scaling down to zero.. Note that
google-cloud-workflows-executions-v1beta is a version-specific client library.
For most uses, we recommend installing the main client library
google-cloud-workflows-executions instead. See the readme for more details.


%package       -n gem-google-cloud-workflows-executions-v1beta-doc
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Workflows Executions V1beta API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-workflows-executions-v1beta
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-workflows-executions-v1beta) = 0.3.0

%description   -n gem-google-cloud-workflows-executions-v1beta-doc
API Client library for the Workflows Executions V1beta API documentation
files.

Workflows link series of serverless tasks together in an order you define.
Combine the power of Google Cloud's APIs, serverless products like Cloud
Functions and Cloud Run, and calls to external APIs to create flexible
serverless applications. Workflows requires no infrastructure management and
scales seamlessly with demand, including scaling down to zero.. Note that
google-cloud-workflows-executions-v1beta is a version-specific client library.
For most uses, we recommend installing the main client library
google-cloud-workflows-executions instead. See the readme for more details.

%description   -n gem-google-cloud-workflows-executions-v1beta-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-workflows-executions-v1beta.


%package       -n gem-google-cloud-datastore-admin-v1
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Firestore in Datastore mode Admin V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-datastore-admin-v1) = 0.4.0

%description   -n gem-google-cloud-datastore-admin-v1
Firestore in Datastore mode is a NoSQL document database built for automatic
scaling, high performance, and ease of application development. Note that
google-cloud-datastore-admin-v1 is a version-specific client library. For most
uses, we recommend installing the main client library
google-cloud-datastore-admin instead. See the readme for more details.


%package       -n gem-google-cloud-datastore-admin-v1-doc
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Firestore in Datastore mode Admin V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-datastore-admin-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-datastore-admin-v1) = 0.4.0

%description   -n gem-google-cloud-datastore-admin-v1-doc
API Client library for the Firestore in Datastore mode Admin V1 API
documentation files.

Firestore in Datastore mode is a NoSQL document database built for automatic
scaling, high performance, and ease of application development. Note that
google-cloud-datastore-admin-v1 is a version-specific client library. For most
uses, we recommend installing the main client library
google-cloud-datastore-admin instead. See the readme for more details.

%description   -n gem-google-cloud-datastore-admin-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-datastore-admin-v1.


%package       -n gem-google-cloud-org-policy-v2
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Organization Policy V2 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-org_policy-v2) = 0.2.0

%description   -n gem-google-cloud-org-policy-v2
The Cloud Org Policy service provides a simple mechanism for organizations to
restrict the allowed configurations across their entire Cloud Resource
hierarchy. Note that google-cloud-org_policy-v2 is a version-specific client
library. For most uses, we recommend installing the main client library
google-cloud-org_policy instead. See the readme for more details.


%package       -n gem-google-cloud-org-policy-v2-doc
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Organization Policy V2 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-org_policy-v2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-org_policy-v2) = 0.2.0

%description   -n gem-google-cloud-org-policy-v2-doc
API Client library for the Organization Policy V2 API documentation files.

The Cloud Org Policy service provides a simple mechanism for organizations to
restrict the allowed configurations across their entire Cloud Resource
hierarchy. Note that google-cloud-org_policy-v2 is a version-specific client
library. For most uses, we recommend installing the main client library
google-cloud-org_policy instead. See the readme for more details.

%description   -n gem-google-cloud-org-policy-v2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-org_policy-v2.


%package       -n gem-google-cloud-service-management
Version:       1.0.1
Release:       alt1
Summary:       API Client library for the Service Management API API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-service_management-v1) >= 0.3 gem(google-cloud-service_management-v1) < 1
Provides:      gem(google-cloud-service_management) = 1.0.1

%description   -n gem-google-cloud-service-management
Google Service Management allows service producers to publish their services on
Google Cloud Platform so that they can be discovered and used by service
consumers.


%package       -n gem-google-cloud-service-management-doc
Version:       1.0.1
Release:       alt1
Summary:       API Client library for the Service Management API API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-service_management
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-service_management) = 1.0.1

%description   -n gem-google-cloud-service-management-doc
API Client library for the Service Management API API documentation
files.

Google Service Management allows service producers to publish their services on
Google Cloud Platform so that they can be discovered and used by service
consumers.

%description   -n gem-google-cloud-service-management-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-service_management.


%package       -n gem-google-cloud-spanner-v1
Version:       0.6.1
Release:       alt1
Summary:       API Client library for the Cloud Spanner V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-spanner-v1) = 0.6.1

%description   -n gem-google-cloud-spanner-v1
Cloud Spanner is a managed, mission-critical, globally consistent and scalable
relational database service. Note that google-cloud-spanner-v1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-spanner instead. See the readme for more details.


%package       -n gem-google-cloud-spanner-v1-doc
Version:       0.6.1
Release:       alt1
Summary:       API Client library for the Cloud Spanner V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-spanner-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-spanner-v1) = 0.6.1

%description   -n gem-google-cloud-spanner-v1-doc
API Client library for the Cloud Spanner V1 API documentation files.

Cloud Spanner is a managed, mission-critical, globally consistent and scalable
relational database service. Note that google-cloud-spanner-v1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-spanner instead. See the readme for more details.

%description   -n gem-google-cloud-spanner-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-spanner-v1.


%package       -n gem-google-cloud-access-approval-v1
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Access Approval V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-access_approval-v1) = 0.4.0

%description   -n gem-google-cloud-access-approval-v1
An API for controlling access to data by Google personnel. Note that
google-cloud-access_approval-v1 is a version-specific client library. For most
uses, we recommend installing the main client library
google-cloud-access_approval instead. See the readme for more details.


%package       -n gem-google-cloud-access-approval-v1-doc
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Access Approval V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-access_approval-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-access_approval-v1) = 0.4.0

%description   -n gem-google-cloud-access-approval-v1-doc
API Client library for the Access Approval V1 API documentation files.

An API for controlling access to data by Google personnel. Note that
google-cloud-access_approval-v1 is a version-specific client library. For most
uses, we recommend installing the main client library
google-cloud-access_approval instead. See the readme for more details.

%description   -n gem-google-cloud-access-approval-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-access_approval-v1.


%package       -n gem-google-cloud-firestore
Version:       2.5.1
Release:       alt1
Summary:       API Client library for Google Cloud Firestore API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-firestore-v1) >= 0.0 gem(google-cloud-firestore-v1) < 1
Requires:      gem(concurrent-ruby) >= 1.0 gem(concurrent-ruby) < 2
Requires:      gem(rbtree) >= 0.4.2 gem(rbtree) < 0.5
Provides:      gem(google-cloud-firestore) = 2.5.1

%description   -n gem-google-cloud-firestore
google-cloud-firestore is the official library for Google Cloud Firestore API.


%package       -n gem-google-cloud-firestore-doc
Version:       2.5.1
Release:       alt1
Summary:       API Client library for Google Cloud Firestore API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-firestore
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-firestore) = 2.5.1

%description   -n gem-google-cloud-firestore-doc
API Client library for Google Cloud Firestore API documentation
files.

google-cloud-firestore is the official library for Google Cloud Firestore API.

%description   -n gem-google-cloud-firestore-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-firestore.


%package       -n gem-google-cloud-talent-v4
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud Talent Solution V4 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-talent-v4) = 0.4.0

%description   -n gem-google-cloud-talent-v4
Transform your job search and candidate matching capabilities with Cloud Talent
Solution, designed to support enterprise talent acquisition technology and
evolve with your growing needs. This AI solution includes features such as Job
Search and Profile Search to provide candidates and employers with an enhanced
talent acquisition experience. Note that google-cloud-talent-v4 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-talent instead. See the readme for more details.


%package       -n gem-google-cloud-talent-v4-doc
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud Talent Solution V4 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-talent-v4
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-talent-v4) = 0.4.0

%description   -n gem-google-cloud-talent-v4-doc
API Client library for the Cloud Talent Solution V4 API documentation
files.

Transform your job search and candidate matching capabilities with Cloud Talent
Solution, designed to support enterprise talent acquisition technology and
evolve with your growing needs. This AI solution includes features such as Job
Search and Profile Search to provide candidates and employers with an enhanced
talent acquisition experience. Note that google-cloud-talent-v4 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-talent instead. See the readme for more details.

%description   -n gem-google-cloud-talent-v4-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-talent-v4.


%package       -n gem-google-cloud-data-labeling-v1beta1
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the AI Platform Data Labeling Service V1beta1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-data_labeling-v1beta1) = 0.3.0

%description   -n gem-google-cloud-data-labeling-v1beta1
AI Platform Data Labeling Service lets you work with human labelers to generate
highly accurate labels for a collection of data that you can use in machine
learning models. Note that google-cloud-data_labeling-v1beta1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-data_labeling instead. See the readme for more
details.


%package       -n gem-google-cloud-data-labeling-v1beta1-doc
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the AI Platform Data Labeling Service V1beta1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-data_labeling-v1beta1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-data_labeling-v1beta1) = 0.3.0

%description   -n gem-google-cloud-data-labeling-v1beta1-doc
API Client library for the AI Platform Data Labeling Service V1beta1 API
documentation files.

AI Platform Data Labeling Service lets you work with human labelers to generate
highly accurate labels for a collection of data that you can use in machine
learning models. Note that google-cloud-data_labeling-v1beta1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-data_labeling instead. See the readme for more
details.

%description   -n gem-google-cloud-data-labeling-v1beta1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-data_labeling-v1beta1.


%package       -n gem-google-cloud-bigquery-reservation-v1
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the BigQuery Reservation V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-bigquery-reservation-v1) = 0.3.0

%description   -n gem-google-cloud-bigquery-reservation-v1
The BigQuery Reservation API provides the mechanisms by which enterprise users
can provision and manage dedicated resources such as slots and BigQuery BI
Engine memory allocations. Note that google-cloud-bigquery-reservation-v1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-bigquery-reservation instead. See the readme for
more details.


%package       -n gem-google-cloud-bigquery-reservation-v1-doc
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the BigQuery Reservation V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-bigquery-reservation-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-bigquery-reservation-v1) = 0.3.0

%description   -n gem-google-cloud-bigquery-reservation-v1-doc
API Client library for the BigQuery Reservation V1 API documentation files.

The BigQuery Reservation API provides the mechanisms by which enterprise users
can provision and manage dedicated resources such as slots and BigQuery BI
Engine memory allocations. Note that google-cloud-bigquery-reservation-v1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-bigquery-reservation instead. See the readme for
more details.

%description   -n gem-google-cloud-bigquery-reservation-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-bigquery-reservation-v1.


%package       -n gem-google-cloud-artifact-registry
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Artifact Registry API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-artifact_registry-v1beta2) >= 0.0 gem(google-cloud-artifact_registry-v1beta2) < 1
Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Provides:      gem(google-cloud-artifact_registry) = 0.2.0

%description   -n gem-google-cloud-artifact-registry
Artifact Registry stores and manages build artifacts in a scalable and
integrated service built on Google infrastructure.


%package       -n gem-google-cloud-artifact-registry-doc
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Artifact Registry API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-artifact_registry
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-artifact_registry) = 0.2.0

%description   -n gem-google-cloud-artifact-registry-doc
API Client library for the Artifact Registry API documentation files.

Artifact Registry stores and manages build artifacts in a scalable and
integrated service built on Google infrastructure.

%description   -n gem-google-cloud-artifact-registry-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-artifact_registry.


%package       -n gem-google-cloud-kms
Version:       2.1.0
Release:       alt1
Summary:       API Client library for the Cloud Key Management Service (KMS) API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-kms-v1) >= 0.0 gem(google-cloud-kms-v1) < 1
Provides:      gem(google-cloud-kms) = 2.1.0

%description   -n gem-google-cloud-kms
Manages keys and performs cryptographic operations in a central cloud service,
for direct use by other cloud resources and applications.


%package       -n gem-google-cloud-kms-doc
Version:       2.1.0
Release:       alt1
Summary:       API Client library for the Cloud Key Management Service (KMS) API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-kms
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-kms) = 2.1.0

%description   -n gem-google-cloud-kms-doc
API Client library for the Cloud Key Management Service (KMS) API documentation
files.

Manages keys and performs cryptographic operations in a central cloud service,
for direct use by other cloud resources and applications.

%description   -n gem-google-cloud-kms-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-kms.


%package       -n gem-google-cloud-container-analysis
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Container Analysis API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-container_analysis-v1) >= 0.0 gem(google-cloud-container_analysis-v1) < 1
Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Provides:      gem(google-cloud-container_analysis) = 1.1.0

%description   -n gem-google-cloud-container-analysis
The Container Analysis API is an implementation of Grafeas. It stores, and
enables querying and retrieval of, critical metadata about all of your software
artifacts.


%package       -n gem-google-cloud-container-analysis-doc
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Container Analysis API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-container_analysis
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-container_analysis) = 1.1.0

%description   -n gem-google-cloud-container-analysis-doc
API Client library for the Container Analysis API documentation files.

The Container Analysis API is an implementation of Grafeas. It stores, and
enables querying and retrieval of, critical metadata about all of your software
artifacts.

%description   -n gem-google-cloud-container-analysis-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-container_analysis.


%package       -n gem-google-iam-credentials
Version:       1.0.0
Release:       alt1
Summary:       API Client library for the IAM Service Account Credentials API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-iam-credentials-v1) >= 0.3 gem(google-iam-credentials-v1) < 1
Provides:      gem(google-iam-credentials) = 1.0.0

%description   -n gem-google-iam-credentials
The Service Account Credentials API creates short-lived credentials for Identity
and Access Management (IAM) service accounts. You can also use this API to sign
JSON Web Tokens (JWTs), as well as blobs of binary data that contain other types
of tokens.


%package       -n gem-google-iam-credentials-doc
Version:       1.0.0
Release:       alt1
Summary:       API Client library for the IAM Service Account Credentials API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-iam-credentials
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-iam-credentials) = 1.0.0

%description   -n gem-google-iam-credentials-doc
API Client library for the IAM Service Account Credentials API documentation
files.

The Service Account Credentials API creates short-lived credentials for Identity
and Access Management (IAM) service accounts. You can also use this API to sign
JSON Web Tokens (JWTs), as well as blobs of binary data that contain other types
of tokens.

%description   -n gem-google-iam-credentials-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-iam-credentials.


%package       -n gem-google-cloud-talent-v4beta1
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud Talent Solution V4beta1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-talent-v4beta1) = 0.4.0

%description   -n gem-google-cloud-talent-v4beta1
Transform your job search and candidate matching capabilities with Cloud Talent
Solution, designed to support enterprise talent acquisition technology and
evolve with your growing needs. This AI solution includes features such as Job
Search and Profile Search to provide candidates and employers with an enhanced
talent acquisition experience. Note that google-cloud-talent-v4beta1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-talent instead. See the readme for more details.


%package       -n gem-google-cloud-talent-v4beta1-doc
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud Talent Solution V4beta1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-talent-v4beta1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-talent-v4beta1) = 0.4.0

%description   -n gem-google-cloud-talent-v4beta1-doc
API Client library for the Cloud Talent Solution V4beta1 API documentation
files.

Transform your job search and candidate matching capabilities with Cloud Talent
Solution, designed to support enterprise talent acquisition technology and
evolve with your growing needs. This AI solution includes features such as Job
Search and Profile Search to provide candidates and employers with an enhanced
talent acquisition experience. Note that google-cloud-talent-v4beta1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-talent instead. See the readme for more details.

%description   -n gem-google-cloud-talent-v4beta1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-talent-v4beta1.


%package       -n gem-google-cloud-vision
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Cloud Vision API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-vision-v1) >= 0.0 gem(google-cloud-vision-v1) < 1
Requires:      gem(google-cloud-vision-v1p3beta1) >= 0.0 gem(google-cloud-vision-v1p3beta1) < 1
Provides:      gem(google-cloud-vision) = 1.1.0

%description   -n gem-google-cloud-vision
Cloud Vision API allows developers to easily integrate vision detection features
within applications, including image labeling, face and landmark detection,
optical character recognition (OCR), and tagging of explicit content.


%package       -n gem-google-cloud-vision-doc
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Cloud Vision API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-vision
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-vision) = 1.1.0

%description   -n gem-google-cloud-vision-doc
API Client library for the Cloud Vision API documentation files.

Cloud Vision API allows developers to easily integrate vision detection features
within applications, including image labeling, face and landmark detection,
optical character recognition (OCR), and tagging of explicit content.

%description   -n gem-google-cloud-vision-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-vision.


%package       -n gem-google-cloud-translate-v2
Version:       0.3.0
Release:       alt1
Summary:       API Client library for Cloud Translation V2 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(faraday) >= 0.17.3 gem(faraday) < 2.0
Requires:      gem(googleapis-common-protos) >= 1.3.10 gem(googleapis-common-protos) < 2.0
Requires:      gem(googleapis-common-protos-types) >= 1.0.5 gem(googleapis-common-protos-types) < 2.0
Requires:      gem(googleauth) >= 0.12 gem(googleauth) < 1
Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Provides:      gem(google-cloud-translate-v2) = 0.3.0

%description   -n gem-google-cloud-translate-v2
Cloud Translation can dynamically translate text between thousands of language
pairs. Translation lets websites and programs programmatically integrate with
the translation service.


%package       -n gem-google-cloud-translate-v2-doc
Version:       0.3.0
Release:       alt1
Summary:       API Client library for Cloud Translation V2 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-translate-v2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-translate-v2) = 0.3.0

%description   -n gem-google-cloud-translate-v2-doc
API Client library for Cloud Translation V2 API documentation files.

Cloud Translation can dynamically translate text between thousands of language
pairs. Translation lets websites and programs programmatically integrate with
the translation service.

%description   -n gem-google-cloud-translate-v2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-translate-v2.


%package       -n gem-google-cloud-resource-manager
Version:       0.36.0
Release:       alt1
Summary:       API Client library for Google Cloud Resource Manager
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.2 gem(google-cloud-core) < 2
Requires:      gem(google-apis-cloudresourcemanager_v1) >= 0.1 gem(google-apis-cloudresourcemanager_v1) < 1
Requires:      gem(googleauth) >= 0.9 gem(googleauth) < 1
Provides:      gem(google-cloud-resource_manager) = 0.36.0

%description   -n gem-google-cloud-resource-manager
google-cloud-resource_manager is the official library for Google Cloud Resource
Manager.


%package       -n gem-google-cloud-resource-manager-doc
Version:       0.36.0
Release:       alt1
Summary:       API Client library for Google Cloud Resource Manager documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-resource_manager
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-resource_manager) = 0.36.0

%description   -n gem-google-cloud-resource-manager-doc
API Client library for Google Cloud Resource Manager documentation
files.

google-cloud-resource_manager is the official library for Google Cloud Resource
Manager.

%description   -n gem-google-cloud-resource-manager-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-resource_manager.


%package       -n gem-google-cloud-data-labeling
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the AI Platform Data Labeling Service API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-data_labeling-v1beta1) >= 0.0 gem(google-cloud-data_labeling-v1beta1) < 1
Provides:      gem(google-cloud-data_labeling) = 0.2.0

%description   -n gem-google-cloud-data-labeling
AI Platform Data Labeling Service lets you work with human labelers to generate
highly accurate labels for a collection of data that you can use in machine
learning models.


%package       -n gem-google-cloud-data-labeling-doc
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the AI Platform Data Labeling Service API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-data_labeling
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-data_labeling) = 0.2.0

%description   -n gem-google-cloud-data-labeling-doc
API Client library for the AI Platform Data Labeling Service API documentation
files.

AI Platform Data Labeling Service lets you work with human labelers to generate
highly accurate labels for a collection of data that you can use in machine
learning models.

%description   -n gem-google-cloud-data-labeling-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-data_labeling.


%package       -n gem-google-cloud-bigquery-storage-v1
Version:       0.6.0
Release:       alt1
Summary:       API Client library for the BigQuery Storage V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-bigquery-storage-v1) = 0.6.0

%description   -n gem-google-cloud-bigquery-storage-v1
The BigQuery Storage API provides fast access to BigQuery managed storage. Note
that google-cloud-bigquery-storage-v1 is a version-specific client library. For
most uses, we recommend installing the main client library
google-cloud-bigquery-storage instead. See the readme for more details.


%package       -n gem-google-cloud-bigquery-storage-v1-doc
Version:       0.6.0
Release:       alt1
Summary:       API Client library for the BigQuery Storage V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-bigquery-storage-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-bigquery-storage-v1) = 0.6.0

%description   -n gem-google-cloud-bigquery-storage-v1-doc
API Client library for the BigQuery Storage V1 API documentation files.

The BigQuery Storage API provides fast access to BigQuery managed storage. Note
that google-cloud-bigquery-storage-v1 is a version-specific client library. For
most uses, we recommend installing the main client library
google-cloud-bigquery-storage instead. See the readme for more details.

%description   -n gem-google-cloud-bigquery-storage-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-bigquery-storage-v1.


%package       -n gem-google-cloud-policy-troubleshooter-v1
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the IAM Policy Troubleshooter V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Requires:      gem(grpc-google-iam-v1) >= 0.6.10 gem(grpc-google-iam-v1) < 2.0
Provides:      gem(google-cloud-policy_troubleshooter-v1) = 0.3.0

%description   -n gem-google-cloud-policy-troubleshooter-v1
Policy Troubleshooter makes it easier to understand why a user has access to a
resource or doesn't have permission to call an API. Given an email, resource,
and permission, Policy Troubleshooter will examine all IAM policies that apply
to the resource. It then reveals whether the member's roles include the
permission on that resource and, if so, which policies bind the member to those
roles. Note that google-cloud-policy_troubleshooter-v1 is a version-specific
client library. For most uses, we recommend installing the main client library
google-cloud-policy_troubleshooter instead. See the readme for more details.


%package       -n gem-google-cloud-policy-troubleshooter-v1-doc
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the IAM Policy Troubleshooter V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-policy_troubleshooter-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-policy_troubleshooter-v1) = 0.3.0

%description   -n gem-google-cloud-policy-troubleshooter-v1-doc
API Client library for the IAM Policy Troubleshooter V1 API documentation
files.

Policy Troubleshooter makes it easier to understand why a user has access to a
resource or doesn't have permission to call an API. Given an email, resource,
and permission, Policy Troubleshooter will examine all IAM policies that apply
to the resource. It then reveals whether the member's roles include the
permission on that resource and, if so, which policies bind the member to those
roles. Note that google-cloud-policy_troubleshooter-v1 is a version-specific
client library. For most uses, we recommend installing the main client library
google-cloud-policy_troubleshooter instead. See the readme for more details.

%description   -n gem-google-cloud-policy-troubleshooter-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-policy_troubleshooter-v1.


%package       -n gem-google-cloud-managed-identities-v1
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Managed Service for Microsoft Active Directory API V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-managed_identities-v1) = 0.3.0

%description   -n gem-google-cloud-managed-identities-v1
The Managed Service for Microsoft Active Directory API is used for managing a
highly available, hardened service running Microsoft Active Directory. Note that
google-cloud-managed_identities-v1 is a version-specific client library. For
most uses, we recommend installing the main client library
google-cloud-managed_identities instead. See the readme for more details.


%package       -n gem-google-cloud-managed-identities-v1-doc
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Managed Service for Microsoft Active Directory API V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-managed_identities-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-managed_identities-v1) = 0.3.0

%description   -n gem-google-cloud-managed-identities-v1-doc
API Client library for the Managed Service for Microsoft Active Directory API V1
API documentation files.

The Managed Service for Microsoft Active Directory API is used for managing a
highly available, hardened service running Microsoft Active Directory. Note that
google-cloud-managed_identities-v1 is a version-specific client library. For
most uses, we recommend installing the main client library
google-cloud-managed_identities instead. See the readme for more details.

%description   -n gem-google-cloud-managed-identities-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-managed_identities-v1.


%package       -n gem-google-cloud-bigquery-storage
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the BigQuery Storage API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-bigquery-storage-v1) >= 0.0 gem(google-cloud-bigquery-storage-v1) < 1
Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Provides:      gem(google-cloud-bigquery-storage) = 1.1.0

%description   -n gem-google-cloud-bigquery-storage
The BigQuery Storage API provides fast access to BigQuery managed storage.


%package       -n gem-google-cloud-bigquery-storage-doc
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the BigQuery Storage API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-bigquery-storage
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-bigquery-storage) = 1.1.0

%description   -n gem-google-cloud-bigquery-storage-doc
API Client library for the BigQuery Storage API documentation files.

The BigQuery Storage API provides fast access to BigQuery managed storage.

%description   -n gem-google-cloud-bigquery-storage-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-bigquery-storage.


%package       -n gem-google-cloud-video-transcoder-v1beta1
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Transcoder V1beta1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-video-transcoder-v1beta1) = 0.2.0

%description   -n gem-google-cloud-video-transcoder-v1beta1
The Transcoder API allows you to convert video files and package them for
optimized delivery to web, mobile and connected TVs. Note that
google-cloud-video-transcoder-v1beta1 is a version-specific client library. For
most uses, we recommend installing the main client library
google-cloud-video-transcoder instead. See the readme for more details.


%package       -n gem-google-cloud-video-transcoder-v1beta1-doc
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Transcoder V1beta1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-video-transcoder-v1beta1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-video-transcoder-v1beta1) = 0.2.0

%description   -n gem-google-cloud-video-transcoder-v1beta1-doc
API Client library for the Transcoder V1beta1 API documentation files.

The Transcoder API allows you to convert video files and package them for
optimized delivery to web, mobile and connected TVs. Note that
google-cloud-video-transcoder-v1beta1 is a version-specific client library. For
most uses, we recommend installing the main client library
google-cloud-video-transcoder instead. See the readme for more details.

%description   -n gem-google-cloud-video-transcoder-v1beta1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-video-transcoder-v1beta1.


%package       -n gem-google-cloud-binary-authorization-v1beta1
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Binary Authorization V1beta1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-binary_authorization-v1beta1) = 0.3.0

%description   -n gem-google-cloud-binary-authorization-v1beta1
Binary Authorization is a service on Google Cloud that provides centralized
software supply-chain security for applications that run on Google Kubernetes
Engine (GKE) and GKE on-prem. Note that
google-cloud-binary_authorization-v1beta1 is a version-specific client library.
For most uses, we recommend installing the main client library
google-cloud-binary_authorization instead. See the readme for more details.


%package       -n gem-google-cloud-binary-authorization-v1beta1-doc
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Binary Authorization V1beta1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-binary_authorization-v1beta1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-binary_authorization-v1beta1) = 0.3.0

%description   -n gem-google-cloud-binary-authorization-v1beta1-doc
API Client library for the Binary Authorization V1beta1 API documentation
files.

Binary Authorization is a service on Google Cloud that provides centralized
software supply-chain security for applications that run on Google Kubernetes
Engine (GKE) and GKE on-prem. Note that
google-cloud-binary_authorization-v1beta1 is a version-specific client library.
For most uses, we recommend installing the main client library
google-cloud-binary_authorization instead. See the readme for more details.

%description   -n gem-google-cloud-binary-authorization-v1beta1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-binary_authorization-v1beta1.


%package       -n gem-google-cloud-recommender-v1
Version:       0.8.0
Release:       alt1
Summary:       API Client library for the Recommender V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-recommender-v1) = 0.8.0

%description   -n gem-google-cloud-recommender-v1
Recommender is a service on Google Cloud that provides usage recommendations for
Cloud products and services. Note that google-cloud-recommender-v1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-recommender instead. See the readme for more
details.


%package       -n gem-google-cloud-recommender-v1-doc
Version:       0.8.0
Release:       alt1
Summary:       API Client library for the Recommender V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-recommender-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-recommender-v1) = 0.8.0

%description   -n gem-google-cloud-recommender-v1-doc
API Client library for the Recommender V1 API documentation files.

Recommender is a service on Google Cloud that provides usage recommendations for
Cloud products and services. Note that google-cloud-recommender-v1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-recommender instead. See the readme for more
details.

%description   -n gem-google-cloud-recommender-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-recommender-v1.


%package       -n gem-google-cloud-bigquery-reservation
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the BigQuery Reservation API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-bigquery-reservation-v1) >= 0.0 gem(google-cloud-bigquery-reservation-v1) < 1
Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Provides:      gem(google-cloud-bigquery-reservation) = 1.1.0

%description   -n gem-google-cloud-bigquery-reservation
The BigQuery Reservation API provides the mechanisms by which enterprise users
can provision and manage dedicated resources such as slots and BigQuery BI
Engine memory allocations.


%package       -n gem-google-cloud-bigquery-reservation-doc
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the BigQuery Reservation API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-bigquery-reservation
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-bigquery-reservation) = 1.1.0

%description   -n gem-google-cloud-bigquery-reservation-doc
API Client library for the BigQuery Reservation API documentation files.

The BigQuery Reservation API provides the mechanisms by which enterprise users
can provision and manage dedicated resources such as slots and BigQuery BI
Engine memory allocations.

%description   -n gem-google-cloud-bigquery-reservation-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-bigquery-reservation.


%package       -n gem-google-cloud-gaming-v1
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Cloud Gaming V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-gaming-v1) = 0.3.0

%description   -n gem-google-cloud-gaming-v1
With Game Servers, studios and publishers can deploy and manage their game
server infrastructure hosted on multiple Agones clusters around the world
through a single interface. Note that google-cloud-gaming-v1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-gaming instead. See the readme for more details.


%package       -n gem-google-cloud-gaming-v1-doc
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Cloud Gaming V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-gaming-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-gaming-v1) = 0.3.0

%description   -n gem-google-cloud-gaming-v1-doc
API Client library for the Cloud Gaming V1 API documentation files.

With Game Servers, studios and publishers can deploy and manage their game
server infrastructure hosted on multiple Agones clusters around the world
through a single interface. Note that google-cloud-gaming-v1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-gaming instead. See the readme for more details.

%description   -n gem-google-cloud-gaming-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-gaming-v1.


%package       -n gem-google-cloud-dialogflow
Version:       1.3.0
Release:       alt1
Summary:       API Client library for the Dialogflow API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-dialogflow-v2) >= 0.8 gem(google-cloud-dialogflow-v2) < 1
Provides:      gem(google-cloud-dialogflow) = 1.3.0

%description   -n gem-google-cloud-dialogflow
Dialogflow is an end-to-end, build-once deploy-everywhere development suite for
creating conversational interfaces for websites, mobile applications, popular
messaging platforms, and IoT devices. You can use it to build interfaces (such
as chatbots and conversational IVR) that enable natural and rich interactions
between your users and your business.


%package       -n gem-google-cloud-dialogflow-doc
Version:       1.3.0
Release:       alt1
Summary:       API Client library for the Dialogflow API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-dialogflow
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-dialogflow) = 1.3.0

%description   -n gem-google-cloud-dialogflow-doc
API Client library for the Dialogflow API documentation files.

Dialogflow is an end-to-end, build-once deploy-everywhere development suite for
creating conversational interfaces for websites, mobile applications, popular
messaging platforms, and IoT devices. You can use it to build interfaces (such
as chatbots and conversational IVR) that enable natural and rich interactions
between your users and your business.

%description   -n gem-google-cloud-dialogflow-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-dialogflow.


%package       -n gem-google-cloud-spanner-admin-instance-v1
Version:       0.3.1
Release:       alt1
Summary:       API Client library for the Cloud Spanner Instance Admin V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Requires:      gem(grpc-google-iam-v1) >= 0.6.10 gem(grpc-google-iam-v1) < 2.0
Provides:      gem(google-cloud-spanner-admin-instance-v1) = 0.3.1

%description   -n gem-google-cloud-spanner-admin-instance-v1
Cloud Spanner is a managed, mission-critical, globally consistent and scalable
relational database service. Note that google-cloud-spanner-admin-instance-v1 is
a version-specific client library. For most uses, we recommend installing the
main client library google-cloud-spanner-admin-instance instead. See the readme
for more details.


%package       -n gem-google-cloud-spanner-admin-instance-v1-doc
Version:       0.3.1
Release:       alt1
Summary:       API Client library for the Cloud Spanner Instance Admin V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-spanner-admin-instance-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-spanner-admin-instance-v1) = 0.3.1

%description   -n gem-google-cloud-spanner-admin-instance-v1-doc
API Client library for the Cloud Spanner Instance Admin V1 API documentation
files.

Cloud Spanner is a managed, mission-critical, globally consistent and scalable
relational database service. Note that google-cloud-spanner-admin-instance-v1 is
a version-specific client library. For most uses, we recommend installing the
main client library google-cloud-spanner-admin-instance instead. See the readme
for more details.

%description   -n gem-google-cloud-spanner-admin-instance-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-spanner-admin-instance-v1.


%package       -n gem-google-cloud-webrisk
Version:       0.6.0
Release:       alt1
Summary:       Obsolete API Client library for Web Risk API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-gax) >= 1.8 gem(google-gax) < 2
Requires:      gem(googleapis-common-protos) >= 1.3.9 gem(googleapis-common-protos) < 2.0
Requires:      gem(googleapis-common-protos-types) >= 1.0.4 gem(googleapis-common-protos-types) < 2.0
Provides:      gem(google-cloud-webrisk) = 0.6.0

%description   -n gem-google-cloud-webrisk
This library is deprecated, and will no longer receive updates. Please use
google-cloud-web_risk instead.


%package       -n gem-google-cloud-webrisk-doc
Version:       0.6.0
Release:       alt1
Summary:       Obsolete API Client library for Web Risk API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-webrisk
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-webrisk) = 0.6.0

%description   -n gem-google-cloud-webrisk-doc
Obsolete API Client library for Web Risk API documentation files.

This library is deprecated, and will no longer receive updates. Please use
google-cloud-web_risk instead.

%description   -n gem-google-cloud-webrisk-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-webrisk.


%package       -n gem-google-cloud-monitoring-dashboard-v1
Version:       0.5.0
Release:       alt1
Summary:       API Client library for the Cloud Monitoring Dashboards V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-monitoring-dashboard-v1) = 0.5.0

%description   -n gem-google-cloud-monitoring-dashboard-v1
Cloud Monitoring collects metrics, events, and metadata from Google Cloud,
Amazon Web Services (AWS), hosted uptime probes, and application
instrumentation. The Dashboards API manages arrangements of display widgets.
Note that google-cloud-monitoring-dashboard-v1 is a version-specific client
library. For most uses, we recommend installing the main client library
google-cloud-monitoring-dashboard instead. See the readme for more details.


%package       -n gem-google-cloud-monitoring-dashboard-v1-doc
Version:       0.5.0
Release:       alt1
Summary:       API Client library for the Cloud Monitoring Dashboards V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-monitoring-dashboard-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-monitoring-dashboard-v1) = 0.5.0

%description   -n gem-google-cloud-monitoring-dashboard-v1-doc
API Client library for the Cloud Monitoring Dashboards V1 API documentation
files.

Cloud Monitoring collects metrics, events, and metadata from Google Cloud,
Amazon Web Services (AWS), hosted uptime probes, and application
instrumentation. The Dashboards API manages arrangements of display widgets.
Note that google-cloud-monitoring-dashboard-v1 is a version-specific client
library. For most uses, we recommend installing the main client library
google-cloud-monitoring-dashboard instead. See the readme for more details.

%description   -n gem-google-cloud-monitoring-dashboard-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-monitoring-dashboard-v1.


%package       -n gem-google-cloud-error-reporting-v1beta1
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud Error Reporting V1beta1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-error_reporting-v1beta1) = 0.4.0

%description   -n gem-google-cloud-error-reporting-v1beta1
The Error Reporting API provides a simple endpoint to report errors from your
running service, and read access to error groups and their associated errors.
Note that google-cloud-error_reporting-v1beta1 is a version-specific client
library. For most uses, we recommend installing the main client library
google-cloud-error_reporting instead. See the readme for more details.


%package       -n gem-google-cloud-error-reporting-v1beta1-doc
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud Error Reporting V1beta1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-error_reporting-v1beta1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-error_reporting-v1beta1) = 0.4.0

%description   -n gem-google-cloud-error-reporting-v1beta1-doc
API Client library for the Cloud Error Reporting V1beta1 API documentation
files.

The Error Reporting API provides a simple endpoint to report errors from your
running service, and read access to error groups and their associated errors.
Note that google-cloud-error_reporting-v1beta1 is a version-specific client
library. For most uses, we recommend installing the main client library
google-cloud-error_reporting instead. See the readme for more details.

%description   -n gem-google-cloud-error-reporting-v1beta1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-error_reporting-v1beta1.


%package       -n gem-google-cloud-video-intelligence-v1p2beta1
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud Video Intelligence V1p2beta1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-video_intelligence-v1p2beta1) = 0.4.0

%description   -n gem-google-cloud-video-intelligence-v1p2beta1
Detects objects, explicit content, and scene changes in videos. It also
specifies the region for annotation and transcribes speech to text. Supports
both asynchronous API and streaming API. Note that
google-cloud-video_intelligence-v1p2beta1 is a version-specific client library.
For most uses, we recommend installing the main client library
google-cloud-video_intelligence instead. See the readme for more details.


%package       -n gem-google-cloud-video-intelligence-v1p2beta1-doc
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud Video Intelligence V1p2beta1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-video_intelligence-v1p2beta1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-video_intelligence-v1p2beta1) = 0.4.0

%description   -n gem-google-cloud-video-intelligence-v1p2beta1-doc
API Client library for the Cloud Video Intelligence V1p2beta1 API documentation
files.

Detects objects, explicit content, and scene changes in videos. It also
specifies the region for annotation and transcribes speech to text. Supports
both asynchronous API and streaming API. Note that
google-cloud-video_intelligence-v1p2beta1 is a version-specific client library.
For most uses, we recommend installing the main client library
google-cloud-video_intelligence instead. See the readme for more details.

%description   -n gem-google-cloud-video-intelligence-v1p2beta1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-video_intelligence-v1p2beta1.


%package       -n gem-google-analytics-admin-v1alpha
Version:       0.7.0
Release:       alt1
Summary:       API Client library for the Google Analytics Admin V1alpha API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-analytics-admin-v1alpha) = 0.7.0

%description   -n gem-google-analytics-admin-v1alpha
The Analytics Admin API allows for programmatic access to the Google Analytics
App+Web configuration data. You can use the Google Analytics Admin API to manage
accounts and App+Web properties. Note that google-analytics-admin-v1alpha is a
version-specific client library. For most uses, we recommend installing the main
client library google-analytics-admin instead. See the readme for more details.


%package       -n gem-google-analytics-admin-v1alpha-doc
Version:       0.7.0
Release:       alt1
Summary:       API Client library for the Google Analytics Admin V1alpha API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-analytics-admin-v1alpha
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-analytics-admin-v1alpha) = 0.7.0

%description   -n gem-google-analytics-admin-v1alpha-doc
API Client library for the Google Analytics Admin V1alpha API documentation
files.

The Analytics Admin API allows for programmatic access to the Google Analytics
App+Web configuration data. You can use the Google Analytics Admin API to manage
accounts and App+Web properties. Note that google-analytics-admin-v1alpha is a
version-specific client library. For most uses, we recommend installing the main
client library google-analytics-admin instead. See the readme for more details.

%description   -n gem-google-analytics-admin-v1alpha-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-analytics-admin-v1alpha.


%package       -n gem-google-cloud-gaming
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Cloud Gaming API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-gaming-v1) >= 0.0 gem(google-cloud-gaming-v1) < 1
Provides:      gem(google-cloud-gaming) = 1.1.0

%description   -n gem-google-cloud-gaming
With Game Servers, studios and publishers can deploy and manage their game
server infrastructure hosted on multiple Agones clusters around the world
through a single interface.


%package       -n gem-google-cloud-gaming-doc
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Cloud Gaming API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-gaming
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-gaming) = 1.1.0

%description   -n gem-google-cloud-gaming-doc
API Client library for the Cloud Gaming API documentation files.

With Game Servers, studios and publishers can deploy and manage their game
server infrastructure hosted on multiple Agones clusters around the world
through a single interface.

%description   -n gem-google-cloud-gaming-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-gaming.


%package       -n gem-google-cloud-service-management-v1
Version:       0.3.1
Release:       alt1
Summary:       API Client library for the Service Management API V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-service_management-v1) = 0.3.1

%description   -n gem-google-cloud-service-management-v1
Google Service Management allows service producers to publish their services on
Google Cloud Platform so that they can be discovered and used by service
consumers. Note that google-cloud-service_management-v1 is a version-specific
client library. For most uses, we recommend installing the main client library
google-cloud-service_management instead. See the readme for more details.


%package       -n gem-google-cloud-service-management-v1-doc
Version:       0.3.1
Release:       alt1
Summary:       API Client library for the Service Management API V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-service_management-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-service_management-v1) = 0.3.1

%description   -n gem-google-cloud-service-management-v1-doc
API Client library for the Service Management API V1 API documentation
files.

Google Service Management allows service producers to publish their services on
Google Cloud Platform so that they can be discovered and used by service
consumers. Note that google-cloud-service_management-v1 is a version-specific
client library. For most uses, we recommend installing the main client library
google-cloud-service_management instead. See the readme for more details.

%description   -n gem-google-cloud-service-management-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-service_management-v1.


%package       -n gem-google-cloud-build
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Cloud Build API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-build-v1) >= 0.0 gem(google-cloud-build-v1) < 1
Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Provides:      gem(google-cloud-build) = 1.1.0

%description   -n gem-google-cloud-build
Cloud Build is a service that executes your builds on Google Cloud Platform
infrastructure. Cloud Build can import source code from Google Cloud Storage,
Cloud Source Repositories, GitHub, or Bitbucket, execute a build to your
specifications, and produce artifacts such as Docker containers or Java
archives.


%package       -n gem-google-cloud-build-doc
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Cloud Build API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-build
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-build) = 1.1.0

%description   -n gem-google-cloud-build-doc
API Client library for the Cloud Build API documentation files.

Cloud Build is a service that executes your builds on Google Cloud Platform
infrastructure. Cloud Build can import source code from Google Cloud Storage,
Cloud Source Repositories, GitHub, or Bitbucket, execute a build to your
specifications, and produce artifacts such as Docker containers or Java
archives.

%description   -n gem-google-cloud-build-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-build.


%package       -n gem-google-cloud-tasks-v2beta2
Version:       0.5.0
Release:       alt1
Summary:       API Client library for the Cloud Tasks V2beta2 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Requires:      gem(grpc-google-iam-v1) >= 0.6.10 gem(grpc-google-iam-v1) < 2.0
Provides:      gem(google-cloud-tasks-v2beta2) = 0.5.0

%description   -n gem-google-cloud-tasks-v2beta2
Cloud Tasks is a fully managed service that allows you to manage the execution,
dispatch and delivery of a large number of distributed tasks. You can
asynchronously perform work outside of a user request. Your tasks can be
executed on App Engine or any arbitrary HTTP endpoint. Note that
google-cloud-tasks-v2beta2 is a version-specific client library. For most uses,
we recommend installing the main client library google-cloud-tasks instead. See
the readme for more details.


%package       -n gem-google-cloud-tasks-v2beta2-doc
Version:       0.5.0
Release:       alt1
Summary:       API Client library for the Cloud Tasks V2beta2 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-tasks-v2beta2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-tasks-v2beta2) = 0.5.0

%description   -n gem-google-cloud-tasks-v2beta2-doc
API Client library for the Cloud Tasks V2beta2 API documentation files.

Cloud Tasks is a fully managed service that allows you to manage the execution,
dispatch and delivery of a large number of distributed tasks. You can
asynchronously perform work outside of a user request. Your tasks can be
executed on App Engine or any arbitrary HTTP endpoint. Note that
google-cloud-tasks-v2beta2 is a version-specific client library. For most uses,
we recommend installing the main client library google-cloud-tasks instead. See
the readme for more details.

%description   -n gem-google-cloud-tasks-v2beta2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-tasks-v2beta2.


%package       -n gem-google-cloud-retail-v2
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Retail V2 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-retail-v2) = 0.3.0

%description   -n gem-google-cloud-retail-v2
Retail enables you to build an end-to-end personalized recommendation system
based on state-of-the-art deep learning ML models, without a need for expertise
in ML or recommendation systems. Note that google-cloud-retail-v2 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-retail instead. See the readme for more details.


%package       -n gem-google-cloud-retail-v2-doc
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Retail V2 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-retail-v2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-retail-v2) = 0.3.0

%description   -n gem-google-cloud-retail-v2-doc
API Client library for the Retail V2 API documentation files.

Retail enables you to build an end-to-end personalized recommendation system
based on state-of-the-art deep learning ML models, without a need for expertise
in ML or recommendation systems. Note that google-cloud-retail-v2 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-retail instead. See the readme for more details.

%description   -n gem-google-cloud-retail-v2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-retail-v2.


%package       -n gem-google-cloud-spanner-admin-database-v1
Version:       0.6.0
Release:       alt1
Summary:       API Client library for the Cloud Spanner Database Admin V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Requires:      gem(grpc-google-iam-v1) >= 0.6.10 gem(grpc-google-iam-v1) < 2.0
Provides:      gem(google-cloud-spanner-admin-database-v1) = 0.6.0

%description   -n gem-google-cloud-spanner-admin-database-v1
Cloud Spanner is a managed, mission-critical, globally consistent and scalable
relational database service. Note that google-cloud-spanner-admin-database-v1 is
a version-specific client library. For most uses, we recommend installing the
main client library google-cloud-spanner-admin-database instead. See the readme
for more details.


%package       -n gem-google-cloud-spanner-admin-database-v1-doc
Version:       0.6.0
Release:       alt1
Summary:       API Client library for the Cloud Spanner Database Admin V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-spanner-admin-database-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-spanner-admin-database-v1) = 0.6.0

%description   -n gem-google-cloud-spanner-admin-database-v1-doc
API Client library for the Cloud Spanner Database Admin V1 API documentation
files.

Cloud Spanner is a managed, mission-critical, globally consistent and scalable
relational database service. Note that google-cloud-spanner-admin-database-v1 is
a version-specific client library. For most uses, we recommend installing the
main client library google-cloud-spanner-admin-database instead. See the readme
for more details.

%description   -n gem-google-cloud-spanner-admin-database-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-spanner-admin-database-v1.


%package       -n gem-google-cloud-functions
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Cloud Functions API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-functions-v1) >= 0.0 gem(google-cloud-functions-v1) < 1
Provides:      gem(google-cloud-functions) = 1.1.0

%description   -n gem-google-cloud-functions
The Cloud Functions API manages lightweight user-provided functions executed in
response to events.


%package       -n gem-google-cloud-functions-doc
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Cloud Functions API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-functions
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-functions) = 1.1.0

%description   -n gem-google-cloud-functions-doc
API Client library for the Cloud Functions API documentation files.

The Cloud Functions API manages lightweight user-provided functions executed in
response to events.

%description   -n gem-google-cloud-functions-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-functions.


%package       -n gem-google-cloud-dataproc-v1
Version:       0.6.0
Release:       alt1
Summary:       API Client library for the Cloud Dataproc V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-dataproc-v1) = 0.6.0

%description   -n gem-google-cloud-dataproc-v1
Manages Hadoop-based clusters and jobs on Google Cloud Platform. Note that
google-cloud-dataproc-v1 is a version-specific client library. For most uses, we
recommend installing the main client library google-cloud-dataproc instead. See
the readme for more details.


%package       -n gem-google-cloud-dataproc-v1-doc
Version:       0.6.0
Release:       alt1
Summary:       API Client library for the Cloud Dataproc V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-dataproc-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-dataproc-v1) = 0.6.0

%description   -n gem-google-cloud-dataproc-v1-doc
API Client library for the Cloud Dataproc V1 API documentation files.

Manages Hadoop-based clusters and jobs on Google Cloud Platform. Note that
google-cloud-dataproc-v1 is a version-specific client library. For most uses, we
recommend installing the main client library google-cloud-dataproc instead. See
the readme for more details.

%description   -n gem-google-cloud-dataproc-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-dataproc-v1.


%package       -n gem-google-cloud-security-center-v1
Version:       0.7.0
Release:       alt1
Summary:       API Client library for the Cloud Security Command Center V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Requires:      gem(grpc-google-iam-v1) >= 0.6.10 gem(grpc-google-iam-v1) < 2.0
Provides:      gem(google-cloud-security_center-v1) = 0.7.0

%description   -n gem-google-cloud-security-center-v1
Security Command Center API provides access to temporal views of assets and
findings within an organization. Note that google-cloud-security_center-v1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-security_center instead. See the readme for more
details.


%package       -n gem-google-cloud-security-center-v1-doc
Version:       0.7.0
Release:       alt1
Summary:       API Client library for the Cloud Security Command Center V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-security_center-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-security_center-v1) = 0.7.0

%description   -n gem-google-cloud-security-center-v1-doc
API Client library for the Cloud Security Command Center V1 API documentation
files.

Security Command Center API provides access to temporal views of assets and
findings within an organization. Note that google-cloud-security_center-v1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-security_center instead. See the readme for more
details.

%description   -n gem-google-cloud-security-center-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-security_center-v1.


%package       -n gem-google-cloud-video-intelligence-v1p1beta1
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud Video Intelligence V1p1beta1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-video_intelligence-v1p1beta1) = 0.4.0

%description   -n gem-google-cloud-video-intelligence-v1p1beta1
Detects objects, explicit content, and scene changes in videos. It also
specifies the region for annotation and transcribes speech to text. Supports
both asynchronous API and streaming API. Note that
google-cloud-video_intelligence-v1p1beta1 is a version-specific client library.
For most uses, we recommend installing the main client library
google-cloud-video_intelligence instead. See the readme for more details.


%package       -n gem-google-cloud-video-intelligence-v1p1beta1-doc
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud Video Intelligence V1p1beta1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-video_intelligence-v1p1beta1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-video_intelligence-v1p1beta1) = 0.4.0

%description   -n gem-google-cloud-video-intelligence-v1p1beta1-doc
API Client library for the Cloud Video Intelligence V1p1beta1 API documentation
files.

Detects objects, explicit content, and scene changes in videos. It also
specifies the region for annotation and transcribes speech to text. Supports
both asynchronous API and streaming API. Note that
google-cloud-video_intelligence-v1p1beta1 is a version-specific client library.
For most uses, we recommend installing the main client library
google-cloud-video_intelligence instead. See the readme for more details.

%description   -n gem-google-cloud-video-intelligence-v1p1beta1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-video_intelligence-v1p1beta1.


%package       -n gem-google-cloud-web-security-scanner-v1
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Web Security Scanner V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-web_security_scanner-v1) = 0.3.0

%description   -n gem-google-cloud-web-security-scanner-v1
Web Security Scanner scans your Compute and App Engine apps for common web
vulnerabilities. Note that google-cloud-web_security_scanner-v1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-web_security_scanner instead. See the readme for
more details.


%package       -n gem-google-cloud-web-security-scanner-v1-doc
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Web Security Scanner V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-web_security_scanner-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-web_security_scanner-v1) = 0.3.0

%description   -n gem-google-cloud-web-security-scanner-v1-doc
API Client library for the Web Security Scanner V1 API documentation files.

Web Security Scanner scans your Compute and App Engine apps for common web
vulnerabilities. Note that google-cloud-web_security_scanner-v1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-web_security_scanner instead. See the readme for
more details.

%description   -n gem-google-cloud-web-security-scanner-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-web_security_scanner-v1.


%package       -n gem-google-cloud-error-reporting
Version:       0.42.0
Release:       alt1
Summary:       API Client library for Stackdriver Error Reporting
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(stackdriver-core) >= 1.3 gem(stackdriver-core) < 2
Requires:      gem(google-cloud-error_reporting-v1beta1) >= 0.0 gem(google-cloud-error_reporting-v1beta1) < 1
Requires:      gem(concurrent-ruby) >= 1.1 gem(concurrent-ruby) < 2
Provides:      gem(google-cloud-error_reporting) = 0.42.0

%description   -n gem-google-cloud-error-reporting
google-cloud-error_reporting is the official library for Stackdriver Error
Reporting.


%package       -n gem-google-cloud-error-reporting-doc
Version:       0.42.0
Release:       alt1
Summary:       API Client library for Stackdriver Error Reporting documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-error_reporting
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-error_reporting) = 0.42.0

%description   -n gem-google-cloud-error-reporting-doc
API Client library for Stackdriver Error Reporting documentation
files.

google-cloud-error_reporting is the official library for Stackdriver Error
Reporting.

%description   -n gem-google-cloud-error-reporting-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-error_reporting.


%package       -n gem-google-cloud-asset-v1
Version:       0.11.0
Release:       alt1
Summary:       API Client library for the Cloud Asset V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Requires:      gem(grpc-google-iam-v1) >= 0.6.10 gem(grpc-google-iam-v1) < 2.0
Provides:      gem(google-cloud-asset-v1) = 0.11.0

%description   -n gem-google-cloud-asset-v1
A metadata inventory service that allows you to view, monitor, and analyze all
your GCP and Anthos assets across projects and services. Note that
google-cloud-asset-v1 is a version-specific client library. For most uses, we
recommend installing the main client library google-cloud-asset instead. See the
readme for more details.


%package       -n gem-google-cloud-asset-v1-doc
Version:       0.11.0
Release:       alt1
Summary:       API Client library for the Cloud Asset V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-asset-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-asset-v1) = 0.11.0

%description   -n gem-google-cloud-asset-v1-doc
API Client library for the Cloud Asset V1 API documentation files.

A metadata inventory service that allows you to view, monitor, and analyze all
your GCP and Anthos assets across projects and services. Note that
google-cloud-asset-v1 is a version-specific client library. For most uses, we
recommend installing the main client library google-cloud-asset instead. See the
readme for more details.

%description   -n gem-google-cloud-asset-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-asset-v1.


%package       -n gem-google-cloud-api-gateway
Version:       0.1.0
Release:       alt1
Summary:       API Client library for the API Gateway API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-api_gateway-v1) >= 0.0 gem(google-cloud-api_gateway-v1) < 1
Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Provides:      gem(google-cloud-api_gateway) = 0.1.0

%description   -n gem-google-cloud-api-gateway
API Gateway enables you to provide secure access to your backend services
through a well-defined REST API that is consistent across all of your services,
regardless of the service implementation. Clients consume your REST APIS to
implement standalone apps for a mobile device or tablet, through apps running in
a browser, or through any other type of app that can make a request to an HTTP
endpoint.


%package       -n gem-google-cloud-api-gateway-doc
Version:       0.1.0
Release:       alt1
Summary:       API Client library for the API Gateway API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-api_gateway
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-api_gateway) = 0.1.0

%description   -n gem-google-cloud-api-gateway-doc
API Client library for the API Gateway API documentation files.

API Gateway enables you to provide secure access to your backend services
through a well-defined REST API that is consistent across all of your services,
regardless of the service implementation. Clients consume your REST APIS to
implement standalone apps for a mobile device or tablet, through apps running in
a browser, or through any other type of app that can make a request to an HTTP
endpoint.

%description   -n gem-google-cloud-api-gateway-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-api_gateway.


%package       -n gem-google-cloud-notebooks-v1beta1
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the AI Platform Notebooks V1beta1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-notebooks-v1beta1) = 0.4.0

%description   -n gem-google-cloud-notebooks-v1beta1
AI Platform Notebooks makes it easy to manage JupyterLab instances through a
protected, publicly available notebook instance URL. A JupyterLab instance is a
Deep Learning virtual machine instance with the latest machine learning and data
science libraries pre-installed. Note that google-cloud-notebooks-v1beta1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-notebooks instead. See the readme for more details.


%package       -n gem-google-cloud-notebooks-v1beta1-doc
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the AI Platform Notebooks V1beta1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-notebooks-v1beta1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-notebooks-v1beta1) = 0.4.0

%description   -n gem-google-cloud-notebooks-v1beta1-doc
API Client library for the AI Platform Notebooks V1beta1 API documentation
files.

AI Platform Notebooks makes it easy to manage JupyterLab instances through a
protected, publicly available notebook instance URL. A JupyterLab instance is a
Deep Learning virtual machine instance with the latest machine learning and data
science libraries pre-installed. Note that google-cloud-notebooks-v1beta1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-notebooks instead. See the readme for more details.

%description   -n gem-google-cloud-notebooks-v1beta1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-notebooks-v1beta1.


%package       -n gem-google-cloud-tasks
Version:       2.2.0
Release:       alt1
Summary:       API Client library for the Cloud Tasks API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-tasks-v2) >= 0.0 gem(google-cloud-tasks-v2) < 1
Requires:      gem(google-cloud-tasks-v2beta2) >= 0.0 gem(google-cloud-tasks-v2beta2) < 1
Requires:      gem(google-cloud-tasks-v2beta3) >= 0.0 gem(google-cloud-tasks-v2beta3) < 1
Provides:      gem(google-cloud-tasks) = 2.2.0

%description   -n gem-google-cloud-tasks
Cloud Tasks is a fully managed service that allows you to manage the execution,
dispatch and delivery of a large number of distributed tasks. You can
asynchronously perform work outside of a user request. Your tasks can be
executed on App Engine or any arbitrary HTTP endpoint.


%package       -n gem-google-cloud-tasks-doc
Version:       2.2.0
Release:       alt1
Summary:       API Client library for the Cloud Tasks API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-tasks
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-tasks) = 2.2.0

%description   -n gem-google-cloud-tasks-doc
API Client library for the Cloud Tasks API documentation files.

Cloud Tasks is a fully managed service that allows you to manage the execution,
dispatch and delivery of a large number of distributed tasks. You can
asynchronously perform work outside of a user request. Your tasks can be
executed on App Engine or any arbitrary HTTP endpoint.

%description   -n gem-google-cloud-tasks-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-tasks.


%package       -n gem-google-cloud-metastore
Version:       0.1.0
Release:       alt1
Summary:       API Client library for the Dataproc Metastore API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-metastore-v1) >= 0.0 gem(google-cloud-metastore-v1) < 1
Requires:      gem(google-cloud-metastore-v1beta) >= 0.0 gem(google-cloud-metastore-v1beta) < 1
Provides:      gem(google-cloud-metastore) = 0.1.0

%description   -n gem-google-cloud-metastore
Dataproc Metastore is a fully managed, highly available within a region,
autohealing serverless Apache Hive metastore (HMS) on Google Cloud for data
analytics products. It supports HMS and serves as a critical component for
managing the metadata of relational entities and provides interoperability
between data processing applications in the open source data ecosystem.


%package       -n gem-google-cloud-metastore-doc
Version:       0.1.0
Release:       alt1
Summary:       API Client library for the Dataproc Metastore API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-metastore
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-metastore) = 0.1.0

%description   -n gem-google-cloud-metastore-doc
API Client library for the Dataproc Metastore API documentation files.

Dataproc Metastore is a fully managed, highly available within a region,
autohealing serverless Apache Hive metastore (HMS) on Google Cloud for data
analytics products. It supports HMS and serves as a critical component for
managing the metadata of relational entities and provides interoperability
between data processing applications in the open source data ecosystem.

%description   -n gem-google-cloud-metastore-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-metastore.


%package       -n gem-google-cloud-dlp
Version:       1.2.0
Release:       alt1
Summary:       API Client library for the Cloud Data Loss Prevention (DLP) API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-dlp-v2) >= 0.2 gem(google-cloud-dlp-v2) < 1
Provides:      gem(google-cloud-dlp) = 1.2.0

%description   -n gem-google-cloud-dlp
Provides methods for detection of privacy-sensitive fragments in text, images,
and Google Cloud Platform storage repositories.


%package       -n gem-google-cloud-dlp-doc
Version:       1.2.0
Release:       alt1
Summary:       API Client library for the Cloud Data Loss Prevention (DLP) API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-dlp
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-dlp) = 1.2.0

%description   -n gem-google-cloud-dlp-doc
API Client library for the Cloud Data Loss Prevention (DLP) API documentation
files.

Provides methods for detection of privacy-sensitive fragments in text, images,
and Google Cloud Platform storage repositories.

%description   -n gem-google-cloud-dlp-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-dlp.


%package       -n gem-grafeas-client
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Grafeas API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(grafeas) >= 1.0 gem(grafeas) < 2
Provides:      gem(grafeas-client) = 0.4.0

%description   -n gem-grafeas-client
grafeas-client is the official library for the Grafeas API.


%package       -n grafeas-client-doc
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Grafeas API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета grafeas-client
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(grafeas-client) = 0.4.0

%description   -n grafeas-client-doc
API Client library for the Grafeas API documentation files.

grafeas-client is the official library for the Grafeas API.

%description   -n grafeas-client-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета grafeas-client.


%package       -n gem-google-cloud-data-catalog
Version:       1.2.0
Release:       alt1
Summary:       API Client library for the Data Catalog API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-data_catalog-v1) >= 0.7 gem(google-cloud-data_catalog-v1) < 1
Provides:      gem(google-cloud-data_catalog) = 1.2.0

%description   -n gem-google-cloud-data-catalog
Data Catalog is a centralized and unified data catalog service for all your
Cloud resources, where users and systems can discover data, explore and curate
its semantics, understand how to act on it, and help govern its usage.


%package       -n gem-google-cloud-data-catalog-doc
Version:       1.2.0
Release:       alt1
Summary:       API Client library for the Data Catalog API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-data_catalog
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-data_catalog) = 1.2.0

%description   -n gem-google-cloud-data-catalog-doc
API Client library for the Data Catalog API documentation files.

Data Catalog is a centralized and unified data catalog service for all your
Cloud resources, where users and systems can discover data, explore and curate
its semantics, understand how to act on it, and help govern its usage.

%description   -n gem-google-cloud-data-catalog-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-data_catalog.


%package       -n gem-google-cloud-billing-budgets-v1beta1
Version:       0.6.0
Release:       alt1
Summary:       API Client library for the Billing Budgets V1beta1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-billing-budgets-v1beta1) = 0.6.0

%description   -n gem-google-cloud-billing-budgets-v1beta1
Provides methods to view, create, and manage Cloud Billing budgets
programmatically at scale. Note that google-cloud-billing-budgets-v1beta1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-billing-budgets instead. See the readme for more
details.


%package       -n gem-google-cloud-billing-budgets-v1beta1-doc
Version:       0.6.0
Release:       alt1
Summary:       API Client library for the Billing Budgets V1beta1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-billing-budgets-v1beta1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-billing-budgets-v1beta1) = 0.6.0

%description   -n gem-google-cloud-billing-budgets-v1beta1-doc
API Client library for the Billing Budgets V1beta1 API documentation
files.

Provides methods to view, create, and manage Cloud Billing budgets
programmatically at scale. Note that google-cloud-billing-budgets-v1beta1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-billing-budgets instead. See the readme for more
details.

%description   -n gem-google-cloud-billing-budgets-v1beta1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-billing-budgets-v1beta1.


%package       -n gem-google-cloud-profiler
Version:       1.0.0
Release:       alt1
Summary:       API Client library for the Cloud Profiler API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-profiler-v2) >= 0.2 gem(google-cloud-profiler-v2) < 1
Provides:      gem(google-cloud-profiler) = 1.0.0

%description   -n gem-google-cloud-profiler
Cloud Profiler is a statistical, low-overhead profiler that continuously gathers
CPU usage and memory-allocation information from your production applications.
It attributes that information to the application's source code, helping you
identify the parts of the application consuming the most resources, and
otherwise illuminating the performance characteristics of the code.


%package       -n gem-google-cloud-profiler-doc
Version:       1.0.0
Release:       alt1
Summary:       API Client library for the Cloud Profiler API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-profiler
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-profiler) = 1.0.0

%description   -n gem-google-cloud-profiler-doc
API Client library for the Cloud Profiler API documentation files.

Cloud Profiler is a statistical, low-overhead profiler that continuously gathers
CPU usage and memory-allocation information from your production applications.
It attributes that information to the application's source code, helping you
identify the parts of the application consuming the most resources, and
otherwise illuminating the performance characteristics of the code.

%description   -n gem-google-cloud-profiler-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-profiler.


%package       -n gem-google-cloud-functions-v1
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Cloud Functions V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Requires:      gem(grpc-google-iam-v1) >= 0.6.10 gem(grpc-google-iam-v1) < 2.0
Provides:      gem(google-cloud-functions-v1) = 0.3.0

%description   -n gem-google-cloud-functions-v1
The Cloud Functions API manages lightweight user-provided functions executed in
response to events. Note that google-cloud-functions-v1 is a version-specific
client library. For most uses, we recommend installing the main client library
google-cloud-functions instead. See the readme for more details.


%package       -n gem-google-cloud-functions-v1-doc
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Cloud Functions V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-functions-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-functions-v1) = 0.3.0

%description   -n gem-google-cloud-functions-v1-doc
API Client library for the Cloud Functions V1 API documentation files.

The Cloud Functions API manages lightweight user-provided functions executed in
response to events. Note that google-cloud-functions-v1 is a version-specific
client library. For most uses, we recommend installing the main client library
google-cloud-functions instead. See the readme for more details.

%description   -n gem-google-cloud-functions-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-functions-v1.


%package       -n gem-google-cloud-debugger-v2
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Cloud Debugger V2 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-debugger-v2) = 0.3.0

%description   -n gem-google-cloud-debugger-v2
The Cloud Debugger API allows applications to interact with the Google Cloud
Debugger backends. It provides two interfaces: the Debugger interface and the
Controller interface. The Controller interface allows you to implement an agent
that sends state data -- for example, the value of program variables and the
call stack -- to Cloud Debugger when the application is running. The Debugger
interface allows you to implement a Cloud Debugger client that allows users to
set and delete the breakpoints at which the state data is collected, as well as
read the data that is captured. Note that google-cloud-debugger-v2 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-debugger instead. See the readme for more details.


%package       -n gem-google-cloud-debugger-v2-doc
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Cloud Debugger V2 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-debugger-v2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-debugger-v2) = 0.3.0

%description   -n gem-google-cloud-debugger-v2-doc
API Client library for the Cloud Debugger V2 API documentation files.

The Cloud Debugger API allows applications to interact with the Google Cloud
Debugger backends. It provides two interfaces: the Debugger interface and the
Controller interface. The Controller interface allows you to implement an agent
that sends state data -- for example, the value of program variables and the
call stack -- to Cloud Debugger when the application is running. The Debugger
interface allows you to implement a Cloud Debugger client that allows users to
set and delete the breakpoints at which the state data is collected, as well as
read the data that is captured. Note that google-cloud-debugger-v2 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-debugger instead. See the readme for more details.

%description   -n gem-google-cloud-debugger-v2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-debugger-v2.


%package       -n gem-google-cloud-domains-v1beta1
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Cloud Domains V1beta1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-domains-v1beta1) = 0.2.0

%description   -n gem-google-cloud-domains-v1beta1
The Cloud Domains API provides registration, management and configuration of
domain names. Note that google-cloud-domains-v1beta1 is a version-specific
client library. For most uses, we recommend installing the main client library
google-cloud-domains instead. See the readme for more details.


%package       -n gem-google-cloud-domains-v1beta1-doc
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Cloud Domains V1beta1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-domains-v1beta1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-domains-v1beta1) = 0.2.0

%description   -n gem-google-cloud-domains-v1beta1-doc
API Client library for the Cloud Domains V1beta1 API documentation files.

The Cloud Domains API provides registration, management and configuration of
domain names. Note that google-cloud-domains-v1beta1 is a version-specific
client library. For most uses, we recommend installing the main client library
google-cloud-domains instead. See the readme for more details.

%description   -n gem-google-cloud-domains-v1beta1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-domains-v1beta1.


%package       -n gem-google-cloud-monitoring-v3
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud Monitoring V3 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-monitoring-v3) = 0.4.0

%description   -n gem-google-cloud-monitoring-v3
Cloud Monitoring collects metrics, events, and metadata from Google Cloud,
Amazon Web Services (AWS), hosted uptime probes, and application
instrumentation. Note that google-cloud-monitoring-v3 is a version-specific
client library. For most uses, we recommend installing the main client library
google-cloud-monitoring instead. See the readme for more details.


%package       -n gem-google-cloud-monitoring-v3-doc
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud Monitoring V3 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-monitoring-v3
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-monitoring-v3) = 0.4.0

%description   -n gem-google-cloud-monitoring-v3-doc
API Client library for the Cloud Monitoring V3 API documentation files.

Cloud Monitoring collects metrics, events, and metadata from Google Cloud,
Amazon Web Services (AWS), hosted uptime probes, and application
instrumentation. Note that google-cloud-monitoring-v3 is a version-specific
client library. For most uses, we recommend installing the main client library
google-cloud-monitoring instead. See the readme for more details.

%description   -n gem-google-cloud-monitoring-v3-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-monitoring-v3.


%package       -n gem-google-cloud-monitoring
Version:       1.2.0
Release:       alt1
Summary:       API Client library for the Cloud Monitoring API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-monitoring-v3) >= 0.4 gem(google-cloud-monitoring-v3) < 1
Requires:      gem(google-cloud-monitoring-dashboard-v1) >= 0.5 gem(google-cloud-monitoring-dashboard-v1) < 1
Provides:      gem(google-cloud-monitoring) = 1.2.0

%description   -n gem-google-cloud-monitoring
Cloud Monitoring collects metrics, events, and metadata from Google Cloud,
Amazon Web Services (AWS), hosted uptime probes, and application
instrumentation.


%package       -n gem-google-cloud-monitoring-doc
Version:       1.2.0
Release:       alt1
Summary:       API Client library for the Cloud Monitoring API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-monitoring
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-monitoring) = 1.2.0

%description   -n gem-google-cloud-monitoring-doc
API Client library for the Cloud Monitoring API documentation files.

Cloud Monitoring collects metrics, events, and metadata from Google Cloud,
Amazon Web Services (AWS), hosted uptime probes, and application
instrumentation.

%description   -n gem-google-cloud-monitoring-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-monitoring.


%package       -n gem-google-cloud-recommender
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Recommender API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-recommender-v1) >= 0.1 gem(google-cloud-recommender-v1) < 1
Provides:      gem(google-cloud-recommender) = 1.1.0

%description   -n gem-google-cloud-recommender
Recommender is a service on Google Cloud that provides usage recommendations for
Cloud products and services.


%package       -n gem-google-cloud-recommender-doc
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Recommender API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-recommender
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-recommender) = 1.1.0

%description   -n gem-google-cloud-recommender-doc
API Client library for the Recommender API documentation files.

Recommender is a service on Google Cloud that provides usage recommendations for
Cloud products and services.

%description   -n gem-google-cloud-recommender-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-recommender.


%package       -n gem-google-cloud-speech-v1
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud Speech-to-Text V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-speech-v1) = 0.4.0

%description   -n gem-google-cloud-speech-v1
Google Speech-to-Text enables developers to convert audio to text by applying
powerful neural network models in an easy-to-use API. The API recognizes more
than 120 languages and variants to support your global user base. You can enable
voice command-and-control, transcribe audio from call centers, and more. It can
process real-time streaming or prerecorded audio, using Google's machine
learning technology. Note that google-cloud-speech-v1 is a version-specific
client library. For most uses, we recommend installing the main client library
google-cloud-speech instead. See the readme for more details.


%package       -n gem-google-cloud-speech-v1-doc
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud Speech-to-Text V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-speech-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-speech-v1) = 0.4.0

%description   -n gem-google-cloud-speech-v1-doc
API Client library for the Cloud Speech-to-Text V1 API documentation
files.

Google Speech-to-Text enables developers to convert audio to text by applying
powerful neural network models in an easy-to-use API. The API recognizes more
than 120 languages and variants to support your global user base. You can enable
voice command-and-control, transcribe audio from call centers, and more. It can
process real-time streaming or prerecorded audio, using Google's machine
learning technology. Note that google-cloud-speech-v1 is a version-specific
client library. For most uses, we recommend installing the main client library
google-cloud-speech instead. See the readme for more details.

%description   -n gem-google-cloud-speech-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-speech-v1.


%package       -n gem-google-cloud-metastore-v1beta
Version:       0.1.0
Release:       alt1
Summary:       API Client library for the Dataproc Metastore V1beta API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-metastore-v1beta) = 0.1.0

%description   -n gem-google-cloud-metastore-v1beta
Dataproc Metastore is a fully managed, highly available within a region,
autohealing serverless Apache Hive metastore (HMS) on Google Cloud for data
analytics products. It supports HMS and serves as a critical component for
managing the metadata of relational entities and provides interoperability
between data processing applications in the open source data ecosystem. Note
that google-cloud-metastore-v1beta is a version-specific client library. For
most uses, we recommend installing the main client library
google-cloud-metastore instead. See the readme for more details.


%package       -n gem-google-cloud-metastore-v1beta-doc
Version:       0.1.0
Release:       alt1
Summary:       API Client library for the Dataproc Metastore V1beta API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-metastore-v1beta
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-metastore-v1beta) = 0.1.0

%description   -n gem-google-cloud-metastore-v1beta-doc
API Client library for the Dataproc Metastore V1beta API documentation
files.

Dataproc Metastore is a fully managed, highly available within a region,
autohealing serverless Apache Hive metastore (HMS) on Google Cloud for data
analytics products. It supports HMS and serves as a critical component for
managing the metadata of relational entities and provides interoperability
between data processing applications in the open source data ecosystem. Note
that google-cloud-metastore-v1beta is a version-specific client library. For
most uses, we recommend installing the main client library
google-cloud-metastore instead. See the readme for more details.

%description   -n gem-google-cloud-metastore-v1beta-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-metastore-v1beta.


%package       -n gem-google-cloud-datastore-v1
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Firestore in Datastore mode V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-datastore-v1) = 0.3.0

%description   -n gem-google-cloud-datastore-v1
Firestore in Datastore mode is a NoSQL document database built for automatic
scaling, high performance, and ease of application development. Note that
google-cloud-datastore-v1 is a version-specific client library. For most uses,
we recommend installing the main client library google-cloud-datastore instead.
See the readme for more details.


%package       -n gem-google-cloud-datastore-v1-doc
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Firestore in Datastore mode V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-datastore-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-datastore-v1) = 0.3.0

%description   -n gem-google-cloud-datastore-v1-doc
API Client library for the Firestore in Datastore mode V1 API documentation
files.

Firestore in Datastore mode is a NoSQL document database built for automatic
scaling, high performance, and ease of application development. Note that
google-cloud-datastore-v1 is a version-specific client library. For most uses,
we recommend installing the main client library google-cloud-datastore instead.
See the readme for more details.

%description   -n gem-google-cloud-datastore-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-datastore-v1.


%package       -n gem-google-cloud-secret-manager
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Secret Manager API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-secret_manager-v1) >= 0.1 gem(google-cloud-secret_manager-v1) < 1
Requires:      gem(google-cloud-secret_manager-v1beta1) >= 0.3 gem(google-cloud-secret_manager-v1beta1) < 1
Provides:      gem(google-cloud-secret_manager) = 1.1.0

%description   -n gem-google-cloud-secret-manager
Secret Manager is a secure and convenient storage system for API keys,
passwords, certificates, and other sensitive data. Secret Manager provides a
central place and single source of truth to manage, access, and audit secrets
across Google Cloud.


%package       -n gem-google-cloud-secret-manager-doc
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Secret Manager API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-secret_manager
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-secret_manager) = 1.1.0

%description   -n gem-google-cloud-secret-manager-doc
API Client library for the Secret Manager API documentation files.

Secret Manager is a secure and convenient storage system for API keys,
passwords, certificates, and other sensitive data. Secret Manager provides a
central place and single source of truth to manage, access, and audit secrets
across Google Cloud.

%description   -n gem-google-cloud-secret-manager-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-secret_manager.


%package       -n gem-google-cloud-network-connectivity-v1alpha1
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Network Connectivity V1alpha1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-network_connectivity-v1alpha1) = 0.4.0

%description   -n gem-google-cloud-network-connectivity-v1alpha1
Network Connectivity is Google's suite of products that provide enterprise
connectivity from your on-premises network or from another cloud provider to
your Virtual Private Cloud (VPC) network. Note that
google-cloud-network_connectivity-v1alpha1 is a version-specific client library.
For most uses, we recommend installing the main client library
google-cloud-network_connectivity instead. See the readme for more details.


%package       -n gem-google-cloud-network-connectivity-v1alpha1-doc
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Network Connectivity V1alpha1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-network_connectivity-v1alpha1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-network_connectivity-v1alpha1) = 0.4.0

%description   -n gem-google-cloud-network-connectivity-v1alpha1-doc
API Client library for the Network Connectivity V1alpha1 API documentation
files.

Network Connectivity is Google's suite of products that provide enterprise
connectivity from your on-premises network or from another cloud provider to
your Virtual Private Cloud (VPC) network. Note that
google-cloud-network_connectivity-v1alpha1 is a version-specific client library.
For most uses, we recommend installing the main client library
google-cloud-network_connectivity instead. See the readme for more details.

%description   -n gem-google-cloud-network-connectivity-v1alpha1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-network_connectivity-v1alpha1.


%package       -n gem-google-cloud-bigtable
Version:       2.6.0
Release:       alt1
Summary:       API Client library for Cloud Bigtable API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-bigtable-admin-v2) >= 0.0 gem(google-cloud-bigtable-admin-v2) < 1
Requires:      gem(google-cloud-bigtable-v2) >= 0.0 gem(google-cloud-bigtable-v2) < 1
Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Provides:      gem(google-cloud-bigtable) = 2.6.0

%description   -n gem-google-cloud-bigtable
google-cloud-bigtable is the official library for Cloud Bigtable API.


%package       -n gem-google-cloud-bigtable-doc
Version:       2.6.0
Release:       alt1
Summary:       API Client library for Cloud Bigtable API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-bigtable
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-bigtable) = 2.6.0

%description   -n gem-google-cloud-bigtable-doc
API Client library for Cloud Bigtable API documentation
files.

google-cloud-bigtable is the official library for Cloud Bigtable API.

%description   -n gem-google-cloud-bigtable-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-bigtable.


%package       -n gem-google-cloud-bigquery-data-transfer
Version:       1.2.0
Release:       alt1
Summary:       API Client library for the BigQuery Data Transfer Service API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-bigquery-data_transfer-v1) >= 0.0 gem(google-cloud-bigquery-data_transfer-v1) < 1
Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Provides:      gem(google-cloud-bigquery-data_transfer) = 1.2.0

%description   -n gem-google-cloud-bigquery-data-transfer
Schedules queries and transfers external data from SaaS applications to Google
BigQuery on a regular basis.


%package       -n gem-google-cloud-bigquery-data-transfer-doc
Version:       1.2.0
Release:       alt1
Summary:       API Client library for the BigQuery Data Transfer Service API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-bigquery-data_transfer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-bigquery-data_transfer) = 1.2.0

%description   -n gem-google-cloud-bigquery-data-transfer-doc
API Client library for the BigQuery Data Transfer Service API documentation
files.

Schedules queries and transfers external data from SaaS applications to Google
BigQuery on a regular basis.

%description   -n gem-google-cloud-bigquery-data-transfer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-bigquery-data_transfer.


%package       -n gem-google-cloud-service-control-v1
Version:       0.3.1
Release:       alt1
Summary:       API Client library for the Service Control API V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-service_control-v1) = 0.3.1

%description   -n gem-google-cloud-service-control-v1
The Service Control API provides control plane functionality to managed
services, such as logging, monitoring, and status checks. Note that
google-cloud-service_control-v1 is a version-specific client library. For most
uses, we recommend installing the main client library
google-cloud-service_control instead. See the readme for more details.


%package       -n gem-google-cloud-service-control-v1-doc
Version:       0.3.1
Release:       alt1
Summary:       API Client library for the Service Control API V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-service_control-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-service_control-v1) = 0.3.1

%description   -n gem-google-cloud-service-control-v1-doc
API Client library for the Service Control API V1 API documentation files.

The Service Control API provides control plane functionality to managed
services, such as logging, monitoring, and status checks. Note that
google-cloud-service_control-v1 is a version-specific client library. For most
uses, we recommend installing the main client library
google-cloud-service_control instead. See the readme for more details.

%description   -n gem-google-cloud-service-control-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-service_control-v1.


%package       -n gem-google-cloud-policy-troubleshooter
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the IAM Policy Troubleshooter API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-policy_troubleshooter-v1) >= 0.0 gem(google-cloud-policy_troubleshooter-v1) < 1
Provides:      gem(google-cloud-policy_troubleshooter) = 1.1.0

%description   -n gem-google-cloud-policy-troubleshooter
Policy Troubleshooter makes it easier to understand why a user has access to a
resource or doesn't have permission to call an API. Given an email, resource,
and permission, Policy Troubleshooter will examine all IAM policies that apply
to the resource. It then reveals whether the member's roles include the
permission on that resource and, if so, which policies bind the member to those
roles.


%package       -n gem-google-cloud-policy-troubleshooter-doc
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the IAM Policy Troubleshooter API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-policy_troubleshooter
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-policy_troubleshooter) = 1.1.0

%description   -n gem-google-cloud-policy-troubleshooter-doc
API Client library for the IAM Policy Troubleshooter API documentation
files.

Policy Troubleshooter makes it easier to understand why a user has access to a
resource or doesn't have permission to call an API. Given an email, resource,
and permission, Policy Troubleshooter will examine all IAM policies that apply
to the resource. It then reveals whether the member's roles include the
permission on that resource and, if so, which policies bind the member to those
roles.

%description   -n gem-google-cloud-policy-troubleshooter-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-policy_troubleshooter.


%package       -n gem-google-cloud-dataqna-v1alpha
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the BigQuery Data QnA V1alpha API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-dataqna-v1alpha) = 0.2.0

%description   -n gem-google-cloud-dataqna-v1alpha
Data QnA is a natural language question and answer service for BigQuery data.
Note that google-cloud-dataqna-v1alpha is a version-specific client library. For
most uses, we recommend installing the main client library google-cloud-dataqna
instead. See the readme for more details.


%package       -n gem-google-cloud-dataqna-v1alpha-doc
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the BigQuery Data QnA V1alpha API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-dataqna-v1alpha
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-dataqna-v1alpha) = 0.2.0

%description   -n gem-google-cloud-dataqna-v1alpha-doc
API Client library for the BigQuery Data QnA V1alpha API documentation
files.

Data QnA is a natural language question and answer service for BigQuery data.
Note that google-cloud-dataqna-v1alpha is a version-specific client library. For
most uses, we recommend installing the main client library google-cloud-dataqna
instead. See the readme for more details.

%description   -n gem-google-cloud-dataqna-v1alpha-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-dataqna-v1alpha.


%package       -n gem-google-analytics-data-v1alpha
Version:       0.8.0
Release:       alt1
Summary:       API Client library for the Google Analytics Data V1alpha API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-analytics-data-v1alpha) = 0.8.0

%description   -n gem-google-analytics-data-v1alpha
The Google Analytics Data API provides programmatic methods to access report
data in Google Analytics App+Web properties. With the Google Analytics Data API,
you can build custom dashboards to display Google Analytics data, automate
complex reporting tasks to save time, and integrate your Google Analytics data
with other business applications. Note that google-analytics-data-v1alpha is a
version-specific client library. For most uses, we recommend installing the main
client library google-analytics-data instead. See the readme for more details.


%package       -n gem-google-analytics-data-v1alpha-doc
Version:       0.8.0
Release:       alt1
Summary:       API Client library for the Google Analytics Data V1alpha API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-analytics-data-v1alpha
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-analytics-data-v1alpha) = 0.8.0

%description   -n gem-google-analytics-data-v1alpha-doc
API Client library for the Google Analytics Data V1alpha API documentation
files.

The Google Analytics Data API provides programmatic methods to access report
data in Google Analytics App+Web properties. With the Google Analytics Data API,
you can build custom dashboards to display Google Analytics data, automate
complex reporting tasks to save time, and integrate your Google Analytics data
with other business applications. Note that google-analytics-data-v1alpha is a
version-specific client library. For most uses, we recommend installing the main
client library google-analytics-data instead. See the readme for more details.

%description   -n gem-google-analytics-data-v1alpha-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-analytics-data-v1alpha.


%package       -n gem-google-cloud-text-to-speech-v1beta1
Version:       0.6.0
Release:       alt1
Summary:       API Client library for the Cloud Text-to-Speech V1beta1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-text_to_speech-v1beta1) = 0.6.0

%description   -n gem-google-cloud-text-to-speech-v1beta1
Text-to-Speech converts text or Speech Synthesis Markup Language (SSML) input
into audio data of natural human speech. Note that
google-cloud-text_to_speech-v1beta1 is a version-specific client library. For
most uses, we recommend installing the main client library
google-cloud-text_to_speech instead. See the readme for more details.


%package       -n gem-google-cloud-text-to-speech-v1beta1-doc
Version:       0.6.0
Release:       alt1
Summary:       API Client library for the Cloud Text-to-Speech V1beta1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-text_to_speech-v1beta1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-text_to_speech-v1beta1) = 0.6.0

%description   -n gem-google-cloud-text-to-speech-v1beta1-doc
API Client library for the Cloud Text-to-Speech V1beta1 API documentation
files.

Text-to-Speech converts text or Speech Synthesis Markup Language (SSML) input
into audio data of natural human speech. Note that
google-cloud-text_to_speech-v1beta1 is a version-specific client library. For
most uses, we recommend installing the main client library
google-cloud-text_to_speech instead. See the readme for more details.

%description   -n gem-google-cloud-text-to-speech-v1beta1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-text_to_speech-v1beta1.


%package       -n gem-google-cloud-video-intelligence
Version:       3.1.0
Release:       alt1
Summary:       API Client library for the Cloud Video Intelligence API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-video_intelligence-v1) >= 0.0 gem(google-cloud-video_intelligence-v1) < 1
Requires:      gem(google-cloud-video_intelligence-v1beta2) >= 0.0 gem(google-cloud-video_intelligence-v1beta2) < 1
Requires:      gem(google-cloud-video_intelligence-v1p1beta1) >= 0.0 gem(google-cloud-video_intelligence-v1p1beta1) < 1
Requires:      gem(google-cloud-video_intelligence-v1p2beta1) >= 0.0 gem(google-cloud-video_intelligence-v1p2beta1) < 1
Provides:      gem(google-cloud-video_intelligence) = 3.1.0

%description   -n gem-google-cloud-video-intelligence
Detects objects, explicit content, and scene changes in videos. It also
specifies the region for annotation and transcribes speech to text. Supports
both asynchronous API and streaming API.


%package       -n gem-google-cloud-video-intelligence-doc
Version:       3.1.0
Release:       alt1
Summary:       API Client library for the Cloud Video Intelligence API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-video_intelligence
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-video_intelligence) = 3.1.0

%description   -n gem-google-cloud-video-intelligence-doc
API Client library for the Cloud Video Intelligence API documentation
files.

Detects objects, explicit content, and scene changes in videos. It also
specifies the region for annotation and transcribes speech to text. Supports
both asynchronous API and streaming API.

%description   -n gem-google-cloud-video-intelligence-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-video_intelligence.


%package       -n gem-google-cloud-build-v1
Version:       0.7.0
Release:       alt1
Summary:       API Client library for the Cloud Build V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-build-v1) = 0.7.0

%description   -n gem-google-cloud-build-v1
Cloud Build is a service that executes your builds on Google Cloud Platform
infrastructure. Cloud Build can import source code from Google Cloud Storage,
Cloud Source Repositories, GitHub, or Bitbucket, execute a build to your
specifications, and produce artifacts such as Docker containers or Java
archives. Note that google-cloud-build-v1 is a version-specific client library.
For most uses, we recommend installing the main client library
google-cloud-build instead. See the readme for more details.


%package       -n gem-google-cloud-build-v1-doc
Version:       0.7.0
Release:       alt1
Summary:       API Client library for the Cloud Build V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-build-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-build-v1) = 0.7.0

%description   -n gem-google-cloud-build-v1-doc
API Client library for the Cloud Build V1 API documentation files.

Cloud Build is a service that executes your builds on Google Cloud Platform
infrastructure. Cloud Build can import source code from Google Cloud Storage,
Cloud Source Repositories, GitHub, or Bitbucket, execute a build to your
specifications, and produce artifacts such as Docker containers or Java
archives. Note that google-cloud-build-v1 is a version-specific client library.
For most uses, we recommend installing the main client library
google-cloud-build instead. See the readme for more details.

%description   -n gem-google-cloud-build-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-build-v1.


%package       -n gem-google-cloud-asset
Version:       1.3.0
Release:       alt1
Summary:       API Client library for the Cloud Asset API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-asset-v1) >= 0.0 gem(google-cloud-asset-v1) < 1
Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Provides:      gem(google-cloud-asset) = 1.3.0

%description   -n gem-google-cloud-asset
A metadata inventory service that allows you to view, monitor, and analyze all
your GCP and Anthos assets across projects and services.


%package       -n gem-google-cloud-asset-doc
Version:       1.3.0
Release:       alt1
Summary:       API Client library for the Cloud Asset API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-asset
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-asset) = 1.3.0

%description   -n gem-google-cloud-asset-doc
API Client library for the Cloud Asset API documentation files.

A metadata inventory service that allows you to view, monitor, and analyze all
your GCP and Anthos assets across projects and services.

%description   -n gem-google-cloud-asset-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-asset.


%package       -n gem-google-cloud-service-directory-v1
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Service Directory V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Requires:      gem(grpc-google-iam-v1) >= 0.6.10 gem(grpc-google-iam-v1) < 2.0
Provides:      gem(google-cloud-service_directory-v1) = 0.3.0

%description   -n gem-google-cloud-service-directory-v1
Service Directory is the single place to register, browse, and resolve
application services. Note that google-cloud-service_directory-v1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-service_directory instead. See the readme for more
details.


%package       -n gem-google-cloud-service-directory-v1-doc
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Service Directory V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-service_directory-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-service_directory-v1) = 0.3.0

%description   -n gem-google-cloud-service-directory-v1-doc
API Client library for the Service Directory V1 API documentation
files.

Service Directory is the single place to register, browse, and resolve
application services. Note that google-cloud-service_directory-v1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-service_directory instead. See the readme for more
details.

%description   -n gem-google-cloud-service-directory-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-service_directory-v1.


%package       -n gem-google-cloud-app-engine-v1
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the App Engine Admin V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-app_engine-v1) = 0.3.0

%description   -n gem-google-cloud-app-engine-v1
The App Engine Admin API provisions and manages your App Engine applications.
Note that google-cloud-app_engine-v1 is a version-specific client library. For
most uses, we recommend installing the main client library
google-cloud-app_engine instead. See the readme for more details.


%package       -n gem-google-cloud-app-engine-v1-doc
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the App Engine Admin V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-app_engine-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-app_engine-v1) = 0.3.0

%description   -n gem-google-cloud-app-engine-v1-doc
API Client library for the App Engine Admin V1 API documentation files.

The App Engine Admin API provisions and manages your App Engine applications.
Note that google-cloud-app_engine-v1 is a version-specific client library. For
most uses, we recommend installing the main client library
google-cloud-app_engine instead. See the readme for more details.

%description   -n gem-google-cloud-app-engine-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-app_engine-v1.


%package       -n gem-google-cloud-app-engine
Version:       1.0.0
Release:       alt1
Summary:       API Client library for the App Engine Admin API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-app_engine-v1) >= 0.3 gem(google-cloud-app_engine-v1) < 1
Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Provides:      gem(google-cloud-app_engine) = 1.0.0

%description   -n gem-google-cloud-app-engine
The App Engine Admin API provisions and manages your App Engine applications.


%package       -n gem-google-cloud-app-engine-doc
Version:       1.0.0
Release:       alt1
Summary:       API Client library for the App Engine Admin API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-app_engine
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-app_engine) = 1.0.0

%description   -n gem-google-cloud-app-engine-doc
API Client library for the App Engine Admin API documentation files.

The App Engine Admin API provisions and manages your App Engine applications.

%description   -n gem-google-cloud-app-engine-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-app_engine.


%package       -n gem-google-cloud-bigtable-v2
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Cloud Bigtable V2 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-bigtable-v2) = 0.3.0

%description   -n gem-google-cloud-bigtable-v2
Cloud Bigtable is a fully managed, scalable NoSQL database service for large
analytical and operational workloads. Note that google-cloud-bigtable-v2 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-bigtable instead. See the readme for more details.


%package       -n gem-google-cloud-bigtable-v2-doc
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Cloud Bigtable V2 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-bigtable-v2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-bigtable-v2) = 0.3.0

%description   -n gem-google-cloud-bigtable-v2-doc
API Client library for the Cloud Bigtable V2 API documentation files.

Cloud Bigtable is a fully managed, scalable NoSQL database service for large
analytical and operational workloads. Note that google-cloud-bigtable-v2 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-bigtable instead. See the readme for more details.

%description   -n gem-google-cloud-bigtable-v2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-bigtable-v2.


%package       -n gem-grafeas
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Grafeas API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(grafeas-v1) >= 0.0 gem(grafeas-v1) < 1
Provides:      gem(grafeas) = 1.1.0

%description   -n gem-grafeas
The Grafeas API stores, and enables querying and retrieval of, critical metadata
about all of your software artifacts.


%package       -n grafeas-doc
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Grafeas API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета grafeas
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(grafeas) = 1.1.0

%description   -n grafeas-doc
API Client library for the Grafeas API documentation files.

The Grafeas API stores, and enables querying and retrieval of, critical metadata
about all of your software artifacts.

%description   -n grafeas-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета grafeas.


%package       -n gem-google-cloud-scheduler-v1
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud Scheduler V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-scheduler-v1) = 0.4.0

%description   -n gem-google-cloud-scheduler-v1
Cloud Scheduler is a fully managed enterprise-grade cron job scheduler. It
allows you to schedule virtually any job, including batch, big data jobs, cloud
infrastructure operations, and more. You can automate everything, including
retries in case of failure to reduce manual toil and intervention. Cloud
Scheduler even acts as a single pane of glass, allowing you to manage all your
automation tasks from one place. Note that google-cloud-scheduler-v1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-scheduler instead. See the readme for more details.


%package       -n gem-google-cloud-scheduler-v1-doc
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud Scheduler V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-scheduler-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-scheduler-v1) = 0.4.0

%description   -n gem-google-cloud-scheduler-v1-doc
API Client library for the Cloud Scheduler V1 API documentation files.

Cloud Scheduler is a fully managed enterprise-grade cron job scheduler. It
allows you to schedule virtually any job, including batch, big data jobs, cloud
infrastructure operations, and more. You can automate everything, including
retries in case of failure to reduce manual toil and intervention. Cloud
Scheduler even acts as a single pane of glass, allowing you to manage all your
automation tasks from one place. Note that google-cloud-scheduler-v1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-scheduler instead. See the readme for more details.

%description   -n gem-google-cloud-scheduler-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-scheduler-v1.


%package       -n gem-google-cloud-talent
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Cloud Talent Solution API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-talent-v4) >= 0.2 gem(google-cloud-talent-v4) < 1
Requires:      gem(google-cloud-talent-v4beta1) >= 0.2 gem(google-cloud-talent-v4beta1) < 1
Provides:      gem(google-cloud-talent) = 1.1.0

%description   -n gem-google-cloud-talent
Transform your job search and candidate matching capabilities with Cloud Talent
Solution, designed to support enterprise talent acquisition technology and
evolve with your growing needs. This AI solution includes features such as Job
Search and Profile Search (Beta) to provide candidates and employers with an
enhanced talent acquisition experience.


%package       -n gem-google-cloud-talent-doc
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Cloud Talent Solution API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-talent
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-talent) = 1.1.0

%description   -n gem-google-cloud-talent-doc
API Client library for the Cloud Talent Solution API documentation
files.

Transform your job search and candidate matching capabilities with Cloud Talent
Solution, designed to support enterprise talent acquisition technology and
evolve with your growing needs. This AI solution includes features such as Job
Search and Profile Search (Beta) to provide candidates and employers with an
enhanced talent acquisition experience.

%description   -n gem-google-cloud-talent-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-talent.


%package       -n gem-google-cloud-channel
Version:       1.0.1
Release:       alt1
Summary:       API Client library for the Cloud Channel API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-channel-v1) >= 0.5 gem(google-cloud-channel-v1) < 1
Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Provides:      gem(google-cloud-channel) = 1.0.1

%description   -n gem-google-cloud-channel
You can use Channel Services to manage your relationships with your partners and
your customers. Channel Services include a console and APIs to view and
provision links between distributors and resellers, customers and entitlements.


%package       -n gem-google-cloud-channel-doc
Version:       1.0.1
Release:       alt1
Summary:       API Client library for the Cloud Channel API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-channel
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-channel) = 1.0.1

%description   -n gem-google-cloud-channel-doc
API Client library for the Cloud Channel API documentation files.

You can use Channel Services to manage your relationships with your partners and
your customers. Channel Services include a console and APIs to view and
provision links between distributors and resellers, customers and entitlements.

%description   -n gem-google-cloud-channel-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-channel.


%package       -n gem-google-cloud-dialogflow-v2
Version:       0.8.1
Release:       alt1
Summary:       API Client library for the Dialogflow V2 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-dialogflow-v2) = 0.8.1

%description   -n gem-google-cloud-dialogflow-v2
Dialogflow is an end-to-end, build-once deploy-everywhere development suite for
creating conversational interfaces for websites, mobile applications, popular
messaging platforms, and IoT devices. You can use it to build interfaces (such
as chatbots and conversational IVR) that enable natural and rich interactions
between your users and your business. Note that google-cloud-dialogflow-v2 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-dialogflow instead. See the readme for more details.


%package       -n gem-google-cloud-dialogflow-v2-doc
Version:       0.8.1
Release:       alt1
Summary:       API Client library for the Dialogflow V2 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-dialogflow-v2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-dialogflow-v2) = 0.8.1

%description   -n gem-google-cloud-dialogflow-v2-doc
API Client library for the Dialogflow V2 API documentation files.

Dialogflow is an end-to-end, build-once deploy-everywhere development suite for
creating conversational interfaces for websites, mobile applications, popular
messaging platforms, and IoT devices. You can use it to build interfaces (such
as chatbots and conversational IVR) that enable natural and rich interactions
between your users and your business. Note that google-cloud-dialogflow-v2 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-dialogflow instead. See the readme for more details.

%description   -n gem-google-cloud-dialogflow-v2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-dialogflow-v2.


%package       -n gem-google-cloud-iot-v1
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Cloud IoT V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Requires:      gem(grpc-google-iam-v1) >= 0.6.10 gem(grpc-google-iam-v1) < 2.0
Provides:      gem(google-cloud-iot-v1) = 0.3.0

%description   -n gem-google-cloud-iot-v1
Registers and manages IoT (Internet of Things) devices that connect to the
Google Cloud Platform. Note that google-cloud-iot-v1 is a version-specific
client library. For most uses, we recommend installing the main client library
google-cloud-iot instead. See the readme for more details.


%package       -n gem-google-cloud-iot-v1-doc
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Cloud IoT V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-iot-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-iot-v1) = 0.3.0

%description   -n gem-google-cloud-iot-v1-doc
API Client library for the Cloud IoT V1 API documentation files.

Registers and manages IoT (Internet of Things) devices that connect to the
Google Cloud Platform. Note that google-cloud-iot-v1 is a version-specific
client library. For most uses, we recommend installing the main client library
google-cloud-iot instead. See the readme for more details.

%description   -n gem-google-cloud-iot-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-iot-v1.


%package       -n gem-google-cloud-retail
Version:       1.0.0
Release:       alt1
Summary:       API Client library for the Retail API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-retail-v2) >= 0.3 gem(google-cloud-retail-v2) < 1
Provides:      gem(google-cloud-retail) = 1.0.0

%description   -n gem-google-cloud-retail
Retail enables you to build an end-to-end personalized recommendation system
based on state-of-the-art deep learning ML models, without a need for expertise
in ML or recommendation systems.


%package       -n gem-google-cloud-retail-doc
Version:       1.0.0
Release:       alt1
Summary:       API Client library for the Retail API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-retail
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-retail) = 1.0.0

%description   -n gem-google-cloud-retail-doc
API Client library for the Retail API documentation files.

Retail enables you to build an end-to-end personalized recommendation system
based on state-of-the-art deep learning ML models, without a need for expertise
in ML or recommendation systems.

%description   -n gem-google-cloud-retail-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-retail.


%package       -n gem-google-cloud-firestore-v1
Version:       0.4.1
Release:       alt1
Summary:       API Client library for the Cloud Firestore V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-firestore-v1) = 0.4.1

%description   -n gem-google-cloud-firestore-v1
Cloud Firestore is a NoSQL document database built for automatic scaling, high
performance, and ease of application development. Note that
google-cloud-firestore-v1 is a version-specific client library. For most uses,
we recommend installing the main client library google-cloud-firestore instead.
See the readme for more details.


%package       -n gem-google-cloud-firestore-v1-doc
Version:       0.4.1
Release:       alt1
Summary:       API Client library for the Cloud Firestore V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-firestore-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-firestore-v1) = 0.4.1

%description   -n gem-google-cloud-firestore-v1-doc
API Client library for the Cloud Firestore V1 API documentation files.

Cloud Firestore is a NoSQL document database built for automatic scaling, high
performance, and ease of application development. Note that
google-cloud-firestore-v1 is a version-specific client library. For most uses,
we recommend installing the main client library google-cloud-firestore instead.
See the readme for more details.

%description   -n gem-google-cloud-firestore-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-firestore-v1.


%package       -n gem-google-cloud-redis-v1
Version:       0.5.0
Release:       alt1
Summary:       API Client library for the Google Cloud Memorystore for Redis V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-redis-v1) = 0.5.0

%description   -n gem-google-cloud-redis-v1
Creates and manages Redis instances on the Google Cloud Platform. Note that
google-cloud-redis-v1 is a version-specific client library. For most uses, we
recommend installing the main client library google-cloud-redis instead. See the
readme for more details.


%package       -n gem-google-cloud-redis-v1-doc
Version:       0.5.0
Release:       alt1
Summary:       API Client library for the Google Cloud Memorystore for Redis V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-redis-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-redis-v1) = 0.5.0

%description   -n gem-google-cloud-redis-v1-doc
API Client library for the Google Cloud Memorystore for Redis V1 API
documentation files.

Creates and manages Redis instances on the Google Cloud Platform. Note that
google-cloud-redis-v1 is a version-specific client library. For most uses, we
recommend installing the main client library google-cloud-redis instead. See the
readme for more details.

%description   -n gem-google-cloud-redis-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-redis-v1.


%package       -n gem-google-cloud-text-to-speech-v1
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud Text-to-Speech V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-text_to_speech-v1) = 0.4.0

%description   -n gem-google-cloud-text-to-speech-v1
Text-to-Speech converts text or Speech Synthesis Markup Language (SSML) input
into audio data of natural human speech. Note that
google-cloud-text_to_speech-v1 is a version-specific client library. For most
uses, we recommend installing the main client library
google-cloud-text_to_speech instead. See the readme for more details.


%package       -n gem-google-cloud-text-to-speech-v1-doc
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud Text-to-Speech V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-text_to_speech-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-text_to_speech-v1) = 0.4.0

%description   -n gem-google-cloud-text-to-speech-v1-doc
API Client library for the Cloud Text-to-Speech V1 API documentation
files.

Text-to-Speech converts text or Speech Synthesis Markup Language (SSML) input
into audio data of natural human speech. Note that
google-cloud-text_to_speech-v1 is a version-specific client library. For most
uses, we recommend installing the main client library
google-cloud-text_to_speech instead. See the readme for more details.

%description   -n gem-google-cloud-text-to-speech-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-text_to_speech-v1.


%package       -n gem-google-cloud-vision-v1p3beta1
Version:       0.5.0
Release:       alt1
Summary:       API Client library for the Cloud Vision V1p3beta1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-vision-v1p3beta1) = 0.5.0

%description   -n gem-google-cloud-vision-v1p3beta1
Cloud Vision API allows developers to easily integrate vision detection features
within applications, including image labeling, face and landmark detection,
optical character recognition (OCR), and tagging of explicit content. Note that
google-cloud-vision-v1p3beta1 is a version-specific client library. For most
uses, we recommend installing the main client library google-cloud-vision
instead. See the readme for more details.


%package       -n gem-google-cloud-vision-v1p3beta1-doc
Version:       0.5.0
Release:       alt1
Summary:       API Client library for the Cloud Vision V1p3beta1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-vision-v1p3beta1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-vision-v1p3beta1) = 0.5.0

%description   -n gem-google-cloud-vision-v1p3beta1-doc
API Client library for the Cloud Vision V1p3beta1 API documentation
files.

Cloud Vision API allows developers to easily integrate vision detection features
within applications, including image labeling, face and landmark detection,
optical character recognition (OCR), and tagging of explicit content. Note that
google-cloud-vision-v1p3beta1 is a version-specific client library. For most
uses, we recommend installing the main client library google-cloud-vision
instead. See the readme for more details.

%description   -n gem-google-cloud-vision-v1p3beta1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-vision-v1p3beta1.


%package       -n gem-google-cloud-language-v1
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Natural Language V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-language-v1) = 0.4.0

%description   -n gem-google-cloud-language-v1
Provides natural language understanding technologies, such as sentiment
analysis, entity recognition, entity sentiment analysis, and other text
annotations. Note that google-cloud-language-v1 is a version-specific client
library. For most uses, we recommend installing the main client library
google-cloud-language instead. See the readme for more details.


%package       -n gem-google-cloud-language-v1-doc
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Natural Language V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-language-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-language-v1) = 0.4.0

%description   -n gem-google-cloud-language-v1-doc
API Client library for the Natural Language V1 API documentation
files.

Provides natural language understanding technologies, such as sentiment
analysis, entity recognition, entity sentiment analysis, and other text
annotations. Note that google-cloud-language-v1 is a version-specific client
library. For most uses, we recommend installing the main client library
google-cloud-language instead. See the readme for more details.

%description   -n gem-google-cloud-language-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-language-v1.


%package       -n gem-google-cloud-tasks-v2
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud Tasks V2 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Requires:      gem(grpc-google-iam-v1) >= 0.6.10 gem(grpc-google-iam-v1) < 2.0
Provides:      gem(google-cloud-tasks-v2) = 0.4.0

%description   -n gem-google-cloud-tasks-v2
Cloud Tasks is a fully managed service that allows you to manage the execution,
dispatch and delivery of a large number of distributed tasks. You can
asynchronously perform work outside of a user request. Your tasks can be
executed on App Engine or any arbitrary HTTP endpoint. Note that
google-cloud-tasks-v2 is a version-specific client library. For most uses, we
recommend installing the main client library google-cloud-tasks instead. See the
readme for more details.


%package       -n gem-google-cloud-tasks-v2-doc
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud Tasks V2 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-tasks-v2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-tasks-v2) = 0.4.0

%description   -n gem-google-cloud-tasks-v2-doc
API Client library for the Cloud Tasks V2 API documentation files.

Cloud Tasks is a fully managed service that allows you to manage the execution,
dispatch and delivery of a large number of distributed tasks. You can
asynchronously perform work outside of a user request. Your tasks can be
executed on App Engine or any arbitrary HTTP endpoint. Note that
google-cloud-tasks-v2 is a version-specific client library. For most uses, we
recommend installing the main client library google-cloud-tasks instead. See the
readme for more details.

%description   -n gem-google-cloud-tasks-v2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-tasks-v2.


%package       -n gem-google-cloud-video-transcoder
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Transcoder API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-video-transcoder-v1beta1) >= 0.0 gem(google-cloud-video-transcoder-v1beta1) < 1
Provides:      gem(google-cloud-video-transcoder) = 0.2.0

%description   -n gem-google-cloud-video-transcoder
The Transcoder API allows you to convert video files and package them for
optimized delivery to web, mobile and connected TVs.


%package       -n gem-google-cloud-video-transcoder-doc
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Transcoder API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-video-transcoder
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-video-transcoder) = 0.2.0

%description   -n gem-google-cloud-video-transcoder-doc
API Client library for the Transcoder API documentation files.

The Transcoder API allows you to convert video files and package them for
optimized delivery to web, mobile and connected TVs.

%description   -n gem-google-cloud-video-transcoder-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-video-transcoder.


%package       -n gem-google-cloud-storage
Version:       1.31.1
Release:       alt1
Summary:       API Client library for Google Cloud Storage
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.2 gem(google-cloud-core) < 2
Requires:      gem(google-apis-iamcredentials_v1) >= 0.1 gem(google-apis-iamcredentials_v1) < 1
Requires:      gem(google-apis-storage_v1) >= 0.1 gem(google-apis-storage_v1) < 1
Requires:      gem(googleauth) >= 0.9 gem(googleauth) < 1
Requires:      gem(digest-crc) >= 0.4 gem(digest-crc) < 1
Requires:      gem(addressable) >= 2.5 gem(addressable) < 3
Requires:      gem(mini_mime) >= 1.0 gem(mini_mime) < 2
Provides:      gem(google-cloud-storage) = 1.31.1

%description   -n gem-google-cloud-storage
google-cloud-storage is the official library for Google Cloud Storage.


%package       -n gem-google-cloud-storage-doc
Version:       1.31.1
Release:       alt1
Summary:       API Client library for Google Cloud Storage documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-storage
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-storage) = 1.31.1

%description   -n gem-google-cloud-storage-doc
API Client library for Google Cloud Storage documentation
files.

google-cloud-storage is the official library for Google Cloud Storage.

%description   -n gem-google-cloud-storage-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-storage.


%package       -n gem-gcloud
Version:       0.24.1
Release:       alt1
Summary:       API Client library for Google Cloud
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud) >= 0.23 gem(google-cloud) < 1
Provides:      gem(gcloud) = 0.24.1

%description   -n gem-gcloud
gcloud is the legacy support library for the new google-cloud library.


%package       -n gem-gcloud-doc
Version:       0.24.1
Release:       alt1
Summary:       API Client library for Google Cloud documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gcloud
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gcloud) = 0.24.1

%description   -n gem-gcloud-doc
API Client library for Google Cloud documentation files.

gcloud is the legacy support library for the new google-cloud library.

%description   -n gem-gcloud-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gcloud.


%package       -n gem-google-cloud-asset-v1beta1
Version:       0.2.5
Release:       alt1
Summary:       API Client library for the Cloud Asset V1beta1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.3 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Requires:      gem(grpc-google-iam-v1) >= 0.6.10 gem(grpc-google-iam-v1) < 2.0
Provides:      gem(google-cloud-asset-v1beta1) = 0.2.5

%description   -n gem-google-cloud-asset-v1beta1
A metadata inventory service that allows you to view, monitor, and analyze all
your GCP and Anthos assets across projects and services.


%package       -n gem-google-cloud-asset-v1beta1-doc
Version:       0.2.5
Release:       alt1
Summary:       API Client library for the Cloud Asset V1beta1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-asset-v1beta1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-asset-v1beta1) = 0.2.5

%description   -n gem-google-cloud-asset-v1beta1-doc
API Client library for the Cloud Asset V1beta1 API documentation files.

A metadata inventory service that allows you to view, monitor, and analyze all
your GCP and Anthos assets across projects and services.

%description   -n gem-google-cloud-asset-v1beta1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-asset-v1beta1.


%package       -n gem-google-cloud-video-intelligence-v1beta2
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud Video Intelligence V1beta2 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-video_intelligence-v1beta2) = 0.4.0

%description   -n gem-google-cloud-video-intelligence-v1beta2
Detects objects, explicit content, and scene changes in videos. It also
specifies the region for annotation and transcribes speech to text. Supports
both asynchronous API and streaming API. Note that
google-cloud-video_intelligence-v1beta2 is a version-specific client library.
For most uses, we recommend installing the main client library
google-cloud-video_intelligence instead. See the readme for more details.


%package       -n gem-google-cloud-video-intelligence-v1beta2-doc
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud Video Intelligence V1beta2 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-video_intelligence-v1beta2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-video_intelligence-v1beta2) = 0.4.0

%description   -n gem-google-cloud-video-intelligence-v1beta2-doc
API Client library for the Cloud Video Intelligence V1beta2 API documentation
files.

Detects objects, explicit content, and scene changes in videos. It also
specifies the region for annotation and transcribes speech to text. Supports
both asynchronous API and streaming API. Note that
google-cloud-video_intelligence-v1beta2 is a version-specific client library.
For most uses, we recommend installing the main client library
google-cloud-video_intelligence instead. See the readme for more details.

%description   -n gem-google-cloud-video-intelligence-v1beta2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-video_intelligence-v1beta2.


%package       -n gem-google-cloud-translate
Version:       3.2.0
Release:       alt1
Summary:       API Client library for the Cloud Translation API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-translate-v2) >= 0.0 gem(google-cloud-translate-v2) < 1
Requires:      gem(google-cloud-translate-v3) >= 0.0 gem(google-cloud-translate-v3) < 1
Provides:      gem(google-cloud-translate) = 3.2.0

%description   -n gem-google-cloud-translate
Cloud Translation can dynamically translate text between thousands of language
pairs. Translation lets websites and programs programmatically integrate with
the translation service.


%package       -n gem-google-cloud-translate-doc
Version:       3.2.0
Release:       alt1
Summary:       API Client library for the Cloud Translation API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-translate
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-translate) = 3.2.0

%description   -n gem-google-cloud-translate-doc
API Client library for the Cloud Translation API documentation files.

Cloud Translation can dynamically translate text between thousands of language
pairs. Translation lets websites and programs programmatically integrate with
the translation service.

%description   -n gem-google-cloud-translate-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-translate.


%package       -n gem-google-cloud-web-security-scanner-v1beta
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Web Security Scanner V1beta API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-web_security_scanner-v1beta) = 0.3.0

%description   -n gem-google-cloud-web-security-scanner-v1beta
Web Security Scanner scans your Compute and App Engine apps for common web
vulnerabilities. Note that google-cloud-web_security_scanner-v1beta is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-web_security_scanner instead. See the readme for
more details.


%package       -n gem-google-cloud-web-security-scanner-v1beta-doc
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Web Security Scanner V1beta API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-web_security_scanner-v1beta
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-web_security_scanner-v1beta) = 0.3.0

%description   -n gem-google-cloud-web-security-scanner-v1beta-doc
API Client library for the Web Security Scanner V1beta API documentation
files.

Web Security Scanner scans your Compute and App Engine apps for common web
vulnerabilities. Note that google-cloud-web_security_scanner-v1beta is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-web_security_scanner instead. See the readme for
more details.

%description   -n gem-google-cloud-web-security-scanner-v1beta-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-web_security_scanner-v1beta.


%package       -n gem-google-cloud-kms-v1
Version:       0.5.0
Release:       alt1
Summary:       API Client library for the Cloud Key Management Service (KMS) V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Requires:      gem(grpc-google-iam-v1) >= 0.6.10 gem(grpc-google-iam-v1) < 2.0
Provides:      gem(google-cloud-kms-v1) = 0.5.0

%description   -n gem-google-cloud-kms-v1
Manages keys and performs cryptographic operations in a central cloud service,
for direct use by other cloud resources and applications. Note that
google-cloud-kms-v1 is a version-specific client library. For most uses, we
recommend installing the main client library google-cloud-kms instead. See the
readme for more details.


%package       -n gem-google-cloud-kms-v1-doc
Version:       0.5.0
Release:       alt1
Summary:       API Client library for the Cloud Key Management Service (KMS) V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-kms-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-kms-v1) = 0.5.0

%description   -n gem-google-cloud-kms-v1-doc
API Client library for the Cloud Key Management Service (KMS) V1 API
documentation files.

Manages keys and performs cryptographic operations in a central cloud service,
for direct use by other cloud resources and applications. Note that
google-cloud-kms-v1 is a version-specific client library. For most uses, we
recommend installing the main client library google-cloud-kms instead. See the
readme for more details.

%description   -n gem-google-cloud-kms-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-kms-v1.


%package       -n gem-google-cloud-datastore
Version:       2.2.0
Release:       alt1
Summary:       API Client library for Google Cloud Datastore
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-datastore-v1) >= 0.0 gem(google-cloud-datastore-v1) < 1
Provides:      gem(google-cloud-datastore) = 2.2.0

%description   -n gem-google-cloud-datastore
google-cloud-datastore is the official library for Google Cloud Datastore.


%package       -n gem-google-cloud-datastore-doc
Version:       2.2.0
Release:       alt1
Summary:       API Client library for Google Cloud Datastore documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-datastore
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-datastore) = 2.2.0

%description   -n gem-google-cloud-datastore-doc
API Client library for Google Cloud Datastore documentation
files.

google-cloud-datastore is the official library for Google Cloud Datastore.

%description   -n gem-google-cloud-datastore-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-datastore.


%package       -n gem-google-cloud-recaptcha-enterprise-v1beta1
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the reCAPTCHA Enterprise V1beta1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-recaptcha_enterprise-v1beta1) = 0.4.0

%description   -n gem-google-cloud-recaptcha-enterprise-v1beta1
reCAPTCHA Enterprise is a service that protects your site from spam and abuse.
Note that google-cloud-recaptcha_enterprise-v1beta1 is a version-specific client
library. For most uses, we recommend installing the main client library
google-cloud-recaptcha_enterprise instead. See the readme for more details.


%package       -n gem-google-cloud-recaptcha-enterprise-v1beta1-doc
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the reCAPTCHA Enterprise V1beta1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-recaptcha_enterprise-v1beta1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-recaptcha_enterprise-v1beta1) = 0.4.0

%description   -n gem-google-cloud-recaptcha-enterprise-v1beta1-doc
API Client library for the reCAPTCHA Enterprise V1beta1 API documentation
files.

reCAPTCHA Enterprise is a service that protects your site from spam and abuse.
Note that google-cloud-recaptcha_enterprise-v1beta1 is a version-specific client
library. For most uses, we recommend installing the main client library
google-cloud-recaptcha_enterprise instead. See the readme for more details.

%description   -n gem-google-cloud-recaptcha-enterprise-v1beta1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-recaptcha_enterprise-v1beta1.


%package       -n gem-google-cloud-api-gateway-v1
Version:       0.1.0
Release:       alt1
Summary:       API Client library for the API Gateway V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-api_gateway-v1) = 0.1.0

%description   -n gem-google-cloud-api-gateway-v1
API Gateway enables you to provide secure access to your backend services
through a well-defined REST API that is consistent across all of your services,
regardless of the service implementation. Clients consume your REST APIS to
implement standalone apps for a mobile device or tablet, through apps running in
a browser, or through any other type of app that can make a request to an HTTP
endpoint. Note that google-cloud-api_gateway-v1 is a version-specific client
library. For most uses, we recommend installing the main client library
google-cloud-api_gateway instead. See the readme for more details.


%package       -n gem-google-cloud-api-gateway-v1-doc
Version:       0.1.0
Release:       alt1
Summary:       API Client library for the API Gateway V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-api_gateway-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-api_gateway-v1) = 0.1.0

%description   -n gem-google-cloud-api-gateway-v1-doc
API Client library for the API Gateway V1 API documentation files.

API Gateway enables you to provide secure access to your backend services
through a well-defined REST API that is consistent across all of your services,
regardless of the service implementation. Clients consume your REST APIS to
implement standalone apps for a mobile device or tablet, through apps running in
a browser, or through any other type of app that can make a request to an HTTP
endpoint. Note that google-cloud-api_gateway-v1 is a version-specific client
library. For most uses, we recommend installing the main client library
google-cloud-api_gateway instead. See the readme for more details.

%description   -n gem-google-cloud-api-gateway-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-api_gateway-v1.


%package       -n gem-google-cloud-bigquery
Version:       1.31.0
Release:       alt1
Summary:       API Client library for Google BigQuery
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(concurrent-ruby) >= 1.0 gem(concurrent-ruby) < 2
Requires:      gem(google-apis-bigquery_v2) >= 0.1 gem(google-apis-bigquery_v2) < 1
Requires:      gem(googleauth) >= 0.9 gem(googleauth) < 1
Requires:      gem(google-cloud-core) >= 1.2 gem(google-cloud-core) < 2
Requires:      gem(mini_mime) >= 1.0 gem(mini_mime) < 2
Provides:      gem(google-cloud-bigquery) = 1.31.0

%description   -n gem-google-cloud-bigquery
google-cloud-bigquery is the official library for Google BigQuery.


%package       -n gem-google-cloud-bigquery-doc
Version:       1.31.0
Release:       alt1
Summary:       API Client library for Google BigQuery documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-bigquery
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-bigquery) = 1.31.0

%description   -n gem-google-cloud-bigquery-doc
API Client library for Google BigQuery documentation
files.

google-cloud-bigquery is the official library for Google BigQuery.

%description   -n gem-google-cloud-bigquery-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-bigquery.


%package       -n gem-google-cloud-bigtable-admin-v2
Version:       0.5.1
Release:       alt1
Summary:       API Client library for the Cloud Bigtable Admin V2 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Requires:      gem(grpc-google-iam-v1) >= 0.6.10 gem(grpc-google-iam-v1) < 2.0
Provides:      gem(google-cloud-bigtable-admin-v2) = 0.5.1

%description   -n gem-google-cloud-bigtable-admin-v2
Cloud Bigtable is a fully managed, scalable NoSQL database service for large
analytical and operational workloads. Note that google-cloud-bigtable-admin-v2
is a version-specific client library. For most uses, we recommend installing the
main client library google-cloud-bigtable-admin instead. See the readme for more
details.


%package       -n gem-google-cloud-bigtable-admin-v2-doc
Version:       0.5.1
Release:       alt1
Summary:       API Client library for the Cloud Bigtable Admin V2 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-bigtable-admin-v2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-bigtable-admin-v2) = 0.5.1

%description   -n gem-google-cloud-bigtable-admin-v2-doc
API Client library for the Cloud Bigtable Admin V2 API documentation
files.

Cloud Bigtable is a fully managed, scalable NoSQL database service for large
analytical and operational workloads. Note that google-cloud-bigtable-admin-v2
is a version-specific client library. For most uses, we recommend installing the
main client library google-cloud-bigtable-admin instead. See the readme for more
details.

%description   -n gem-google-cloud-bigtable-admin-v2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-bigtable-admin-v2.


%package       -n gem-google-cloud-network-connectivity
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Network Connectivity API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-network_connectivity-v1alpha1) >= 0.0 gem(google-cloud-network_connectivity-v1alpha1) < 1
Provides:      gem(google-cloud-network_connectivity) = 0.2.0

%description   -n gem-google-cloud-network-connectivity
Network Connectivity is Google's suite of products that provide enterprise
connectivity from your on-premises network or from another cloud provider to
your Virtual Private Cloud (VPC) network.


%package       -n gem-google-cloud-network-connectivity-doc
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Network Connectivity API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-network_connectivity
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-network_connectivity) = 0.2.0

%description   -n gem-google-cloud-network-connectivity-doc
API Client library for the Network Connectivity API documentation
files.

Network Connectivity is Google's suite of products that provide enterprise
connectivity from your on-premises network or from another cloud provider to
your Virtual Private Cloud (VPC) network.

%description   -n gem-google-cloud-network-connectivity-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-network_connectivity.


%package       -n gem-google-cloud-media-translation-v1beta1
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Media Translation V1beta1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-media_translation-v1beta1) = 0.4.0

%description   -n gem-google-cloud-media-translation-v1beta1
Media Translation API delivers real-time speech translation to your content and
applications directly from your audio data. Leveraging Google's machine learning
technologies, the API offers enhanced accuracy and simplified integration while
equipping you with a comprehensive set of features to further refine your
translation results. Improve user experience with low-latency streaming
translation and scale quickly with straightforward internationalization. Note
that google-cloud-media_translation-v1beta1 is a version-specific client
library. For most uses, we recommend installing the main client library
google-cloud-media_translation instead. See the readme for more details.


%package       -n gem-google-cloud-media-translation-v1beta1-doc
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Media Translation V1beta1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-media_translation-v1beta1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-media_translation-v1beta1) = 0.4.0

%description   -n gem-google-cloud-media-translation-v1beta1-doc
API Client library for the Media Translation V1beta1 API documentation
files.

Media Translation API delivers real-time speech translation to your content and
applications directly from your audio data. Leveraging Google's machine learning
technologies, the API offers enhanced accuracy and simplified integration while
equipping you with a comprehensive set of features to further refine your
translation results. Improve user experience with low-latency streaming
translation and scale quickly with straightforward internationalization. Note
that google-cloud-media_translation-v1beta1 is a version-specific client
library. For most uses, we recommend installing the main client library
google-cloud-media_translation instead. See the readme for more details.

%description   -n gem-google-cloud-media-translation-v1beta1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-media_translation-v1beta1.


%package       -n gem-google-cloud-os-config-v1
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud OS Config V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-os_config-v1) = 0.4.0

%description   -n gem-google-cloud-os-config-v1
Cloud OS Config provides OS management tools that can be used for patch
management, patch compliance, and configuration management on VM instances. Note
that google-cloud-os_config-v1 is a version-specific client library. For most
uses, we recommend installing the main client library google-cloud-os_config
instead. See the readme for more details.


%package       -n gem-google-cloud-os-config-v1-doc
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud OS Config V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-os_config-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-os_config-v1) = 0.4.0

%description   -n gem-google-cloud-os-config-v1-doc
API Client library for the Cloud OS Config V1 API documentation files.

Cloud OS Config provides OS management tools that can be used for patch
management, patch compliance, and configuration management on VM instances. Note
that google-cloud-os_config-v1 is a version-specific client library. For most
uses, we recommend installing the main client library google-cloud-os_config
instead. See the readme for more details.

%description   -n gem-google-cloud-os-config-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-os_config-v1.


%package       -n gem-google-cloud-web-risk-v1
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Web Risk V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-web_risk-v1) = 0.4.0

%description   -n gem-google-cloud-web-risk-v1
Web Risk is an enterprise security product that lets your client applications
check URLs against Google's constantly updated lists of unsafe web resources.
Note that google-cloud-web_risk-v1 is a version-specific client library. For
most uses, we recommend installing the main client library google-cloud-web_risk
instead. See the readme for more details.


%package       -n gem-google-cloud-web-risk-v1-doc
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Web Risk V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-web_risk-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-web_risk-v1) = 0.4.0

%description   -n gem-google-cloud-web-risk-v1-doc
API Client library for the Web Risk V1 API documentation files.

Web Risk is an enterprise security product that lets your client applications
check URLs against Google's constantly updated lists of unsafe web resources.
Note that google-cloud-web_risk-v1 is a version-specific client library. For
most uses, we recommend installing the main client library google-cloud-web_risk
instead. See the readme for more details.

%description   -n gem-google-cloud-web-risk-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-web_risk-v1.


%package       -n gem-google-cloud-pubsub
Version:       2.6.1
Release:       alt1
Summary:       API Client library for Google Cloud Pub/Sub
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(concurrent-ruby) >= 1.1 gem(concurrent-ruby) < 2
Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-pubsub-v1) >= 0.0 gem(google-cloud-pubsub-v1) < 1
Provides:      gem(google-cloud-pubsub) = 2.6.1

%description   -n gem-google-cloud-pubsub
google-cloud-pubsub is the official library for Google Cloud Pub/Sub.


%package       -n gem-google-cloud-pubsub-doc
Version:       2.6.1
Release:       alt1
Summary:       API Client library for Google Cloud Pub/Sub documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-pubsub
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-pubsub) = 2.6.1

%description   -n gem-google-cloud-pubsub-doc
API Client library for Google Cloud Pub/Sub documentation
files.

google-cloud-pubsub is the official library for Google Cloud Pub/Sub.

%description   -n gem-google-cloud-pubsub-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-pubsub.


%package       -n gem-google-cloud-security-private-ca-v1beta1
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Certificate Authority Service V1beta1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-security-private_ca-v1beta1) = 0.3.0

%description   -n gem-google-cloud-security-private-ca-v1beta1
Certificate Authority Service is a highly available, scalable Google Cloud
service that enables you to simplify, automate, and customize the deployment,
management, and security of private certificate authorities (CA). Note that
google-cloud-security-private_ca-v1beta1 is a version-specific client library.
For most uses, we recommend installing the main client library
google-cloud-security-private_ca instead. See the readme for more details.


%package       -n gem-google-cloud-security-private-ca-v1beta1-doc
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Certificate Authority Service V1beta1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-security-private_ca-v1beta1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-security-private_ca-v1beta1) = 0.3.0

%description   -n gem-google-cloud-security-private-ca-v1beta1-doc
API Client library for the Certificate Authority Service V1beta1 API
documentation files.

Certificate Authority Service is a highly available, scalable Google Cloud
service that enables you to simplify, automate, and customize the deployment,
management, and security of private certificate authorities (CA). Note that
google-cloud-security-private_ca-v1beta1 is a version-specific client library.
For most uses, we recommend installing the main client library
google-cloud-security-private_ca instead. See the readme for more details.

%description   -n gem-google-cloud-security-private-ca-v1beta1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-security-private_ca-v1beta1.


%package       -n gem-google-cloud-service-control
Version:       0.2.1
Release:       alt1
Summary:       API Client library for the Service Control API API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-service_control-v1) >= 0.0 gem(google-cloud-service_control-v1) < 1
Provides:      gem(google-cloud-service_control) = 0.2.1

%description   -n gem-google-cloud-service-control
The Service Control API provides control plane functionality to managed
services, such as logging, monitoring, and status checks.


%package       -n gem-google-cloud-service-control-doc
Version:       0.2.1
Release:       alt1
Summary:       API Client library for the Service Control API API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-service_control
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-service_control) = 0.2.1

%description   -n gem-google-cloud-service-control-doc
API Client library for the Service Control API API documentation files.

The Service Control API provides control plane functionality to managed
services, such as logging, monitoring, and status checks.

%description   -n gem-google-cloud-service-control-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-service_control.


%package       -n gem-google-cloud-iot
Version:       1.0.0
Release:       alt1
Summary:       API Client library for the Cloud IoT API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-iot-v1) >= 0.3 gem(google-cloud-iot-v1) < 1
Provides:      gem(google-cloud-iot) = 1.0.0

%description   -n gem-google-cloud-iot
Registers and manages IoT (Internet of Things) devices that connect to the
Google Cloud Platform.


%package       -n gem-google-cloud-iot-doc
Version:       1.0.0
Release:       alt1
Summary:       API Client library for the Cloud IoT API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-iot
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-iot) = 1.0.0

%description   -n gem-google-cloud-iot-doc
API Client library for the Cloud IoT API documentation files.

Registers and manages IoT (Internet of Things) devices that connect to the
Google Cloud Platform.

%description   -n gem-google-cloud-iot-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-iot.


%package       -n gem-google-cloud-service-directory-v1beta1
Version:       0.6.0
Release:       alt1
Summary:       API Client library for the Service Directory V1beta1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Requires:      gem(grpc-google-iam-v1) >= 0.6.10 gem(grpc-google-iam-v1) < 2.0
Provides:      gem(google-cloud-service_directory-v1beta1) = 0.6.0

%description   -n gem-google-cloud-service-directory-v1beta1
Service directory is the single place to register, browse, and resolve
application services. Note that google-cloud-service_directory-v1beta1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-service_directory instead. See the readme for more
details.


%package       -n gem-google-cloud-service-directory-v1beta1-doc
Version:       0.6.0
Release:       alt1
Summary:       API Client library for the Service Directory V1beta1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-service_directory-v1beta1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-service_directory-v1beta1) = 0.6.0

%description   -n gem-google-cloud-service-directory-v1beta1-doc
API Client library for the Service Directory V1beta1 API documentation
files.

Service directory is the single place to register, browse, and resolve
application services. Note that google-cloud-service_directory-v1beta1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-service_directory instead. See the readme for more
details.

%description   -n gem-google-cloud-service-directory-v1beta1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-service_directory-v1beta1.


%package       -n gem-google-iam-credentials-v1
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the IAM Service Account Credentials V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-iam-credentials-v1) = 0.3.0

%description   -n gem-google-iam-credentials-v1
The Service Account Credentials API creates short-lived credentials for Identity
and Access Management (IAM) service accounts. You can also use this API to sign
JSON Web Tokens (JWTs), as well as blobs of binary data that contain other types
of tokens. Note that google-iam-credentials-v1 is a version-specific client
library. For most uses, we recommend installing the main client library
google-iam-credentials instead. See the readme for more details.


%package       -n gem-google-iam-credentials-v1-doc
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the IAM Service Account Credentials V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-iam-credentials-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-iam-credentials-v1) = 0.3.0

%description   -n gem-google-iam-credentials-v1-doc
API Client library for the IAM Service Account Credentials V1 API documentation
files.

The Service Account Credentials API creates short-lived credentials for Identity
and Access Management (IAM) service accounts. You can also use this API to sign
JSON Web Tokens (JWTs), as well as blobs of binary data that contain other types
of tokens. Note that google-iam-credentials-v1 is a version-specific client
library. For most uses, we recommend installing the main client library
google-iam-credentials instead. See the readme for more details.

%description   -n gem-google-iam-credentials-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-iam-credentials-v1.


%package       -n gem-google-cloud-logging-v2
Version:       0.5.0
Release:       alt1
Summary:       API Client library for the Cloud Logging V2 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-logging-v2) = 0.5.0

%description   -n gem-google-cloud-logging-v2
The Cloud Logging API lets you programmatically read and write log entries, set
up exclusions, create logs-based metrics, and manage export sinks. Note that
google-cloud-logging-v2 is a version-specific client library. For most uses, we
recommend installing the main client library google-cloud-logging instead. See
the readme for more details.


%package       -n gem-google-cloud-logging-v2-doc
Version:       0.5.0
Release:       alt1
Summary:       API Client library for the Cloud Logging V2 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-logging-v2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-logging-v2) = 0.5.0

%description   -n gem-google-cloud-logging-v2-doc
API Client library for the Cloud Logging V2 API documentation files.

The Cloud Logging API lets you programmatically read and write log entries, set
up exclusions, create logs-based metrics, and manage export sinks. Note that
google-cloud-logging-v2 is a version-specific client library. For most uses, we
recommend installing the main client library google-cloud-logging instead. See
the readme for more details.

%description   -n gem-google-cloud-logging-v2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-logging-v2.


%package       -n gem-google-cloud-access-approval
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Access Approval API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-access_approval-v1) >= 0.0 gem(google-cloud-access_approval-v1) < 1
Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Provides:      gem(google-cloud-access_approval) = 1.1.0

%description   -n gem-google-cloud-access-approval
An API for controlling access to data by Google personnel.


%package       -n gem-google-cloud-access-approval-doc
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Access Approval API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-access_approval
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-access_approval) = 1.1.0

%description   -n gem-google-cloud-access-approval-doc
API Client library for the Access Approval API documentation files.

An API for controlling access to data by Google personnel.

%description   -n gem-google-cloud-access-approval-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-access_approval.


%package       -n gem-google-cloud-redis-v1beta1
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Google Cloud Memorystore for Redis V1beta1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-redis-v1beta1) = 0.4.0

%description   -n gem-google-cloud-redis-v1beta1
Creates and manages Redis instances on the Google Cloud Platform. Note that
google-cloud-redis-v1beta1 is a version-specific client library. For most uses,
we recommend installing the main client library google-cloud-redis instead. See
the readme for more details.


%package       -n gem-google-cloud-redis-v1beta1-doc
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Google Cloud Memorystore for Redis V1beta1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-redis-v1beta1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-redis-v1beta1) = 0.4.0

%description   -n gem-google-cloud-redis-v1beta1-doc
API Client library for the Google Cloud Memorystore for Redis V1beta1 API
documentation files.

Creates and manages Redis instances on the Google Cloud Platform. Note that
google-cloud-redis-v1beta1 is a version-specific client library. For most uses,
we recommend installing the main client library google-cloud-redis instead. See
the readme for more details.

%description   -n gem-google-cloud-redis-v1beta1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-redis-v1beta1.


%package       -n gem-google-cloud-os-login-v1beta
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud OS Login V1beta API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-os_login-v1beta) = 0.4.0

%description   -n gem-google-cloud-os-login-v1beta
Use OS Login to manage SSH access to your instances using IAM without having to
create and manage individual SSH keys. OS Login maintains a consistent Linux
user identity across VM instances and is the recommended way to manage many
users across multiple instances or projects. Note that
google-cloud-os_login-v1beta is a version-specific client library. For most
uses, we recommend installing the main client library google-cloud-os_login
instead. See the readme for more details.


%package       -n gem-google-cloud-os-login-v1beta-doc
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud OS Login V1beta API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-os_login-v1beta
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-os_login-v1beta) = 0.4.0

%description   -n gem-google-cloud-os-login-v1beta-doc
API Client library for the Cloud OS Login V1beta API documentation files.

Use OS Login to manage SSH access to your instances using IAM without having to
create and manage individual SSH keys. OS Login maintains a consistent Linux
user identity across VM instances and is the recommended way to manage many
users across multiple instances or projects. Note that
google-cloud-os_login-v1beta is a version-specific client library. For most
uses, we recommend installing the main client library google-cloud-os_login
instead. See the readme for more details.

%description   -n gem-google-cloud-os-login-v1beta-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-os_login-v1beta.


%package       -n gem-google-cloud-speech-v1p1beta1
Version:       0.9.0
Release:       alt1
Summary:       API Client library for the Cloud Speech-to-Text V1p1beta1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-speech-v1p1beta1) = 0.9.0

%description   -n gem-google-cloud-speech-v1p1beta1
Google Speech-to-Text enables developers to convert audio to text by applying
powerful neural network models in an easy-to-use API. The API recognizes more
than 120 languages and variants to support your global user base. You can enable
voice command-and-control, transcribe audio from call centers, and more. It can
process real-time streaming or prerecorded audio, using Google's machine
learning technology. Note that google-cloud-speech-v1p1beta1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-speech instead. See the readme for more details.


%package       -n gem-google-cloud-speech-v1p1beta1-doc
Version:       0.9.0
Release:       alt1
Summary:       API Client library for the Cloud Speech-to-Text V1p1beta1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-speech-v1p1beta1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-speech-v1p1beta1) = 0.9.0

%description   -n gem-google-cloud-speech-v1p1beta1-doc
API Client library for the Cloud Speech-to-Text V1p1beta1 API documentation
files.

Google Speech-to-Text enables developers to convert audio to text by applying
powerful neural network models in an easy-to-use API. The API recognizes more
than 120 languages and variants to support your global user base. You can enable
voice command-and-control, transcribe audio from call centers, and more. It can
process real-time streaming or prerecorded audio, using Google's machine
learning technology. Note that google-cloud-speech-v1p1beta1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-speech instead. See the readme for more details.

%description   -n gem-google-cloud-speech-v1p1beta1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-speech-v1p1beta1.


%package       -n gem-google-cloud-notebooks
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the AI Platform Notebooks API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-notebooks-v1beta1) >= 0.0 gem(google-cloud-notebooks-v1beta1) < 1
Provides:      gem(google-cloud-notebooks) = 1.1.0

%description   -n gem-google-cloud-notebooks
AI Platform Notebooks makes it easy to manage JupyterLab instances through a
protected, publicly available notebook instance URL. A JupyterLab instance is a
Deep Learning virtual machine instance with the latest machine learning and data
science libraries pre-installed.


%package       -n gem-google-cloud-notebooks-doc
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the AI Platform Notebooks API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-notebooks
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-notebooks) = 1.1.0

%description   -n gem-google-cloud-notebooks-doc
API Client library for the AI Platform Notebooks API documentation files.

AI Platform Notebooks makes it easy to manage JupyterLab instances through a
protected, publicly available notebook instance URL. A JupyterLab instance is a
Deep Learning virtual machine instance with the latest machine learning and data
science libraries pre-installed.

%description   -n gem-google-cloud-notebooks-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-notebooks.


%package       -n gem-google-cloud-billing
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Billing API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-billing-v1) >= 0.1 gem(google-cloud-billing-v1) < 1
Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Provides:      gem(google-cloud-billing) = 1.1.0

%description   -n gem-google-cloud-billing
Allows developers to manage billing for their Google Cloud Platform projects
programmatically.


%package       -n gem-google-cloud-billing-doc
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Billing API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-billing
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-billing) = 1.1.0

%description   -n gem-google-cloud-billing-doc
API Client library for the Billing API documentation files.

Allows developers to manage billing for their Google Cloud Platform projects
programmatically.

%description   -n gem-google-cloud-billing-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-billing.


%package       -n gem-google-cloud-gke-hub-v1beta1
Version:       0.1.0
Release:       alt1
Summary:       API Client library for the GKE Hub V1beta1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-gke_hub-v1beta1) = 0.1.0

%description   -n gem-google-cloud-gke-hub-v1beta1
The GKE Hub API centrally manages features and services on all your Kubernetes
clusters running in a variety of environments, including Google cloud, on
premises in customer datacenters, or other third party clouds. Note that
google-cloud-gke_hub-v1beta1 is a version-specific client library. For most
uses, we recommend installing the main client library google-cloud-gke_hub
instead. See the readme for more details.


%package       -n gem-google-cloud-gke-hub-v1beta1-doc
Version:       0.1.0
Release:       alt1
Summary:       API Client library for the GKE Hub V1beta1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-gke_hub-v1beta1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-gke_hub-v1beta1) = 0.1.0

%description   -n gem-google-cloud-gke-hub-v1beta1-doc
API Client library for the GKE Hub V1beta1 API documentation files.

The GKE Hub API centrally manages features and services on all your Kubernetes
clusters running in a variety of environments, including Google cloud, on
premises in customer datacenters, or other third party clouds. Note that
google-cloud-gke_hub-v1beta1 is a version-specific client library. For most
uses, we recommend installing the main client library google-cloud-gke_hub
instead. See the readme for more details.

%description   -n gem-google-cloud-gke-hub-v1beta1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-gke_hub-v1beta1.


%package       -n gem-google-cloud-document-ai
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Document AI API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-document_ai-v1beta3) >= 0.0 gem(google-cloud-document_ai-v1beta3) < 1
Provides:      gem(google-cloud-document_ai) = 0.3.0

%description   -n gem-google-cloud-document-ai
Document AI uses machine learning on a single cloud-based platform to
automatically classify, extract, and enrich data within your documents to unlock
insights.


%package       -n gem-google-cloud-document-ai-doc
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Document AI API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-document_ai
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-document_ai) = 0.3.0

%description   -n gem-google-cloud-document-ai-doc
API Client library for the Document AI API documentation files.

Document AI uses machine learning on a single cloud-based platform to
automatically classify, extract, and enrich data within your documents to unlock
insights.

%description   -n gem-google-cloud-document-ai-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-document_ai.


%package       -n gem-google-cloud-data-catalog-v1
Version:       0.7.1
Release:       alt1
Summary:       API Client library for the Data Catalog V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Requires:      gem(grpc-google-iam-v1) >= 0.6.10 gem(grpc-google-iam-v1) < 2.0
Provides:      gem(google-cloud-data_catalog-v1) = 0.7.1

%description   -n gem-google-cloud-data-catalog-v1
DataCatalog is a centralized and unified data catalog service for all your Cloud
resources, where users and systems can discover data, explore and curate its
semantics, understand how to act on it, and help govern its usage. Note that
google-cloud-data_catalog-v1 is a version-specific client library. For most
uses, we recommend installing the main client library google-cloud-data_catalog
instead. See the readme for more details.


%package       -n gem-google-cloud-data-catalog-v1-doc
Version:       0.7.1
Release:       alt1
Summary:       API Client library for the Data Catalog V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-data_catalog-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-data_catalog-v1) = 0.7.1

%description   -n gem-google-cloud-data-catalog-v1-doc
API Client library for the Data Catalog V1 API documentation files.

DataCatalog is a centralized and unified data catalog service for all your Cloud
resources, where users and systems can discover data, explore and curate its
semantics, understand how to act on it, and help govern its usage. Note that
google-cloud-data_catalog-v1 is a version-specific client library. For most
uses, we recommend installing the main client library google-cloud-data_catalog
instead. See the readme for more details.

%description   -n gem-google-cloud-data-catalog-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-data_catalog-v1.


%package       -n gem-google-area120-tables
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Area 120 Tables API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-area120-tables-v1alpha1) >= 0.0 gem(google-area120-tables-v1alpha1) < 1
Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Provides:      gem(google-area120-tables) = 0.2.0

%description   -n gem-google-area120-tables
Using the Area 120 Tables API, you can query for tables, and
update/create/delete rows within tables programmatically.


%package       -n gem-google-area120-tables-doc
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Area 120 Tables API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-area120-tables
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-area120-tables) = 0.2.0

%description   -n gem-google-area120-tables-doc
API Client library for the Area 120 Tables API documentation files.

Using the Area 120 Tables API, you can query for tables, and
update/create/delete rows within tables programmatically.

%description   -n gem-google-area120-tables-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-area120-tables.


%package       -n gem-google-cloud-trace-v1
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Cloud Trace V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-trace-v1) = 0.3.0

%description   -n gem-google-cloud-trace-v1
The Cloud Trace API lets you send and retrieve latency data to and from Cloud
Trace. This API provides low-level interfaces for interacting directly with the
feature. For some languages, you can use OpenCensus, a set of open source
tracing and stats instrumentation libraries that work with multiple backends.
Note that google-cloud-trace-v1 is a version-specific client library. For most
uses, we recommend installing the main client library google-cloud-trace
instead. See the readme for more details.


%package       -n gem-google-cloud-trace-v1-doc
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Cloud Trace V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-trace-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-trace-v1) = 0.3.0

%description   -n gem-google-cloud-trace-v1-doc
API Client library for the Cloud Trace V1 API documentation files.

The Cloud Trace API lets you send and retrieve latency data to and from Cloud
Trace. This API provides low-level interfaces for interacting directly with the
feature. For some languages, you can use OpenCensus, a set of open source
tracing and stats instrumentation libraries that work with multiple backends.
Note that google-cloud-trace-v1 is a version-specific client library. For most
uses, we recommend installing the main client library google-cloud-trace
instead. See the readme for more details.

%description   -n gem-google-cloud-trace-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-trace-v1.


%package       -n gem-google-cloud-debugger
Version:       0.42.0
Release:       alt1
Summary:       API Client and instrumentation library for Stackdriver Debugger
Group:         Development/Ruby

Requires:      gem(binding_of_caller) >= 0.7 gem(binding_of_caller) < 2
Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-debugger-v2) >= 0.0 gem(google-cloud-debugger-v2) < 1
Requires:      gem(google-cloud-logging) >= 2.0 gem(google-cloud-logging) < 3
Requires:      gem(stackdriver-core) >= 1.3 gem(stackdriver-core) < 2
Requires:      gem(concurrent-ruby) >= 1.1 gem(concurrent-ruby) < 2
Provides:      gem(google-cloud-debugger) = 0.42.0

%description   -n gem-google-cloud-debugger
google-cloud-debugger is the official library for Stackdriver Debugger.


%package       -n gem-google-cloud-debugger-doc
Version:       0.42.0
Release:       alt1
Summary:       API Client and instrumentation library for Stackdriver Debugger documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-debugger
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-debugger) = 0.42.0

%description   -n gem-google-cloud-debugger-doc
API Client and instrumentation library for Stackdriver Debugger documentation
files.

google-cloud-debugger is the official library for Stackdriver Debugger.

%description   -n gem-google-cloud-debugger-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-debugger.


%package       -n gem-google-cloud
Version:       0.64.0
Release:       alt1
Summary:       API Client library for Google Cloud
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-asset) >= 1.0 gem(google-cloud-asset) < 2
Requires:      gem(google-cloud-bigquery) >= 1.1 gem(google-cloud-bigquery) < 2
Requires:      gem(google-cloud-bigquery-data_transfer) >= 1.0 gem(google-cloud-bigquery-data_transfer) < 2
Requires:      gem(google-cloud-bigtable) >= 2.0 gem(google-cloud-bigtable) < 3
Requires:      gem(google-cloud-container) >= 1.0 gem(google-cloud-container) < 2
Requires:      gem(google-cloud-dataproc) >= 1.0 gem(google-cloud-dataproc) < 2
Requires:      gem(google-cloud-datastore) >= 2.0 gem(google-cloud-datastore) < 3
Requires:      gem(google-cloud-dialogflow) >= 1.0 gem(google-cloud-dialogflow) < 2
Requires:      gem(google-cloud-dlp) >= 1.0 gem(google-cloud-dlp) < 2
Requires:      gem(google-cloud-dns) >= 0.28 gem(google-cloud-dns) < 1
Requires:      gem(google-cloud-error_reporting) >= 0.30 gem(google-cloud-error_reporting) < 1
Requires:      gem(google-cloud-firestore) >= 2.0 gem(google-cloud-firestore) < 3
Requires:      gem(google-cloud-kms) >= 2.0 gem(google-cloud-kms) < 3
Requires:      gem(google-cloud-language) >= 1.0 gem(google-cloud-language) < 2
Requires:      gem(google-cloud-logging) >= 2.0 gem(google-cloud-logging) < 3
Requires:      gem(google-cloud-monitoring) >= 1.0 gem(google-cloud-monitoring) < 2
Requires:      gem(google-cloud-os_login) >= 1.0 gem(google-cloud-os_login) < 2
Requires:      gem(google-cloud-phishing_protection) >= 0.1 gem(google-cloud-phishing_protection) < 1
Requires:      gem(google-cloud-pubsub) >= 2.0 gem(google-cloud-pubsub) < 3
Requires:      gem(google-cloud-recaptcha_enterprise) >= 1.0 gem(google-cloud-recaptcha_enterprise) < 2
Requires:      gem(google-cloud-redis) >= 1.0 gem(google-cloud-redis) < 2
Requires:      gem(google-cloud-resource_manager) >= 0.29 gem(google-cloud-resource_manager) < 1
Requires:      gem(google-cloud-scheduler) >= 2.0 gem(google-cloud-scheduler) < 3
Requires:      gem(google-cloud-security_center) >= 1.0 gem(google-cloud-security_center) < 2
Requires:      gem(google-cloud-spanner) >= 2.0 gem(google-cloud-spanner) < 3
Requires:      gem(google-cloud-speech) >= 1.0 gem(google-cloud-speech) < 2
Requires:      gem(google-cloud-storage) >= 1.10 gem(google-cloud-storage) < 2
Requires:      gem(google-cloud-talent) >= 1.0 gem(google-cloud-talent) < 2
Requires:      gem(google-cloud-tasks) >= 2.0 gem(google-cloud-tasks) < 3
Requires:      gem(google-cloud-text_to_speech) >= 1.0 gem(google-cloud-text_to_speech) < 2
Requires:      gem(google-cloud-trace) >= 0.31 gem(google-cloud-trace) < 1
Requires:      gem(google-cloud-translate) >= 3.0 gem(google-cloud-translate) < 4
Requires:      gem(google-cloud-video_intelligence) >= 3.0 gem(google-cloud-video_intelligence) < 4
Requires:      gem(google-cloud-vision) >= 1.0 gem(google-cloud-vision) < 2
Provides:      gem(google-cloud) = 0.64.0

%description   -n gem-google-cloud
google-cloud is the official library for Google Cloud Platform APIs.


%package       -n gem-google-cloud-doc
Version:       0.64.0
Release:       alt1
Summary:       API Client library for Google Cloud documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud) = 0.64.0

%description   -n gem-google-cloud-doc
API Client library for Google Cloud documentation files.

google-cloud is the official library for Google Cloud Platform APIs.

%description   -n gem-google-cloud-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud.


%package       -n gem-google-cloud-recommendation-engine
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Recommendations AI API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-recommendation_engine-v1beta1) >= 0.0 gem(google-cloud-recommendation_engine-v1beta1) < 1
Provides:      gem(google-cloud-recommendation_engine) = 0.2.0

%description   -n gem-google-cloud-recommendation-engine
Recommendations AI enables you to build an end-to-end personalized
recommendation system based on state-of-the-art deep learning ML models, without
a need for expertise in ML or recommendation systems.


%package       -n gem-google-cloud-recommendation-engine-doc
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Recommendations AI API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-recommendation_engine
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-recommendation_engine) = 0.2.0

%description   -n gem-google-cloud-recommendation-engine-doc
API Client library for the Recommendations AI API documentation
files.

Recommendations AI enables you to build an end-to-end personalized
recommendation system based on state-of-the-art deep learning ML models, without
a need for expertise in ML or recommendation systems.

%description   -n gem-google-cloud-recommendation-engine-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-recommendation_engine.


%package       -n gem-google-cloud-container-analysis-v1
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Container Analysis V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Requires:      gem(grafeas-v1) >= 0.0 gem(grafeas-v1) < 1
Requires:      gem(grpc-google-iam-v1) >= 0.6.10 gem(grpc-google-iam-v1) < 2.0
Provides:      gem(google-cloud-container_analysis-v1) = 0.4.0

%description   -n gem-google-cloud-container-analysis-v1
The Container Analysis API is an implementation of Grafeas. It stores, and
enables querying and retrieval of, critical metadata about all of your software
artifacts. Note that google-cloud-container_analysis-v1 is a version-specific
client library. For most uses, we recommend installing the main client library
google-cloud-container_analysis instead. See the readme for more details.


%package       -n gem-google-cloud-container-analysis-v1-doc
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Container Analysis V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-container_analysis-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-container_analysis-v1) = 0.4.0

%description   -n gem-google-cloud-container-analysis-v1-doc
API Client library for the Container Analysis V1 API documentation files.

The Container Analysis API is an implementation of Grafeas. It stores, and
enables querying and retrieval of, critical metadata about all of your software
artifacts. Note that google-cloud-container_analysis-v1 is a version-specific
client library. For most uses, we recommend installing the main client library
google-cloud-container_analysis instead. See the readme for more details.

%description   -n gem-google-cloud-container-analysis-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-container_analysis-v1.


%package       -n gem-google-cloud-phishing-protection-v1beta1
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Phishing Protection V1beta1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-phishing_protection-v1beta1) = 0.3.0

%description   -n gem-google-cloud-phishing-protection-v1beta1
Phishing Protection helps prevent users from accessing phishing sites by
identifying various signals associated with malicious content, including the use
of your brand assets, classifying malicious content that uses your brand and
reporting the unsafe URLs to Google Safe Browsing. Note that
google-cloud-phishing_protection-v1beta1 is a version-specific client library.
For most uses, we recommend installing the main client library
google-cloud-phishing_protection instead. See the readme for more details.


%package       -n gem-google-cloud-phishing-protection-v1beta1-doc
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Phishing Protection V1beta1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-phishing_protection-v1beta1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-phishing_protection-v1beta1) = 0.3.0

%description   -n gem-google-cloud-phishing-protection-v1beta1-doc
API Client library for the Phishing Protection V1beta1 API documentation
files.

Phishing Protection helps prevent users from accessing phishing sites by
identifying various signals associated with malicious content, including the use
of your brand assets, classifying malicious content that uses your brand and
reporting the unsafe URLs to Google Safe Browsing. Note that
google-cloud-phishing_protection-v1beta1 is a version-specific client library.
For most uses, we recommend installing the main client library
google-cloud-phishing_protection instead. See the readme for more details.

%description   -n gem-google-cloud-phishing-protection-v1beta1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-phishing_protection-v1beta1.


%package       -n gem-google-cloud-os-config
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Cloud OS Config API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-os_config-v1) >= 0.0 gem(google-cloud-os_config-v1) < 1
Provides:      gem(google-cloud-os_config) = 1.1.0

%description   -n gem-google-cloud-os-config
Cloud OS Config provides OS management tools that can be used for patch
management, patch compliance, and configuration management on VM instances.


%package       -n gem-google-cloud-os-config-doc
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Cloud OS Config API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-os_config
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-os_config) = 1.1.0

%description   -n gem-google-cloud-os-config-doc
API Client library for the Cloud OS Config API documentation files.

Cloud OS Config provides OS management tools that can be used for patch
management, patch compliance, and configuration management on VM instances.

%description   -n gem-google-cloud-os-config-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-os_config.


%package       -n gem-google-cloud-redis
Version:       1.2.0
Release:       alt1
Summary:       API Client library for the Google Cloud Memorystore for Redis API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-redis-v1) >= 0.0 gem(google-cloud-redis-v1) < 1
Requires:      gem(google-cloud-redis-v1beta1) >= 0.0 gem(google-cloud-redis-v1beta1) < 1
Provides:      gem(google-cloud-redis) = 1.2.0

%description   -n gem-google-cloud-redis
Creates and manages Redis instances on the Google Cloud Platform.


%package       -n gem-google-cloud-redis-doc
Version:       1.2.0
Release:       alt1
Summary:       API Client library for the Google Cloud Memorystore for Redis API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-redis
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-redis) = 1.2.0

%description   -n gem-google-cloud-redis-doc
API Client library for the Google Cloud Memorystore for Redis API documentation
files.

Creates and manages Redis instances on the Google Cloud Platform.

%description   -n gem-google-cloud-redis-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-redis.


%package       -n gem-google-cloud-spanner
Version:       2.6.0
Release:       alt1
Summary:       API Client library for Google Cloud Spanner API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-spanner-admin-database-v1) >= 0.1 gem(google-cloud-spanner-admin-database-v1) < 1
Requires:      gem(google-cloud-spanner-admin-instance-v1) >= 0.1 gem(google-cloud-spanner-admin-instance-v1) < 1
Requires:      gem(google-cloud-spanner-v1) >= 0.2 gem(google-cloud-spanner-v1) < 1
Requires:      gem(concurrent-ruby) >= 1.0 gem(concurrent-ruby) < 2
Provides:      gem(google-cloud-spanner) = 2.6.0

%description   -n gem-google-cloud-spanner
google-cloud-spanner is the official library for Google Cloud Spanner API.


%package       -n gem-google-cloud-spanner-doc
Version:       2.6.0
Release:       alt1
Summary:       API Client library for Google Cloud Spanner API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-spanner
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-spanner) = 2.6.0

%description   -n gem-google-cloud-spanner-doc
API Client library for Google Cloud Spanner API documentation
files.

google-cloud-spanner is the official library for Google Cloud Spanner API.

%description   -n gem-google-cloud-spanner-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-spanner.


%package       -n gem-google-cloud-translate-v3
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Cloud Translation V3 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-translate-v3) = 0.3.0

%description   -n gem-google-cloud-translate-v3
Cloud Translation can dynamically translate text between thousands of language
pairs. Translation lets websites and programs programmatically integrate with
the translation service. Note that google-cloud-translate-v3 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-translate instead. See the readme for more details.


%package       -n gem-google-cloud-translate-v3-doc
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Cloud Translation V3 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-translate-v3
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-translate-v3) = 0.3.0

%description   -n gem-google-cloud-translate-v3-doc
API Client library for the Cloud Translation V3 API documentation files.

Cloud Translation can dynamically translate text between thousands of language
pairs. Translation lets websites and programs programmatically integrate with
the translation service. Note that google-cloud-translate-v3 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-translate instead. See the readme for more details.

%description   -n gem-google-cloud-translate-v3-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-translate-v3.


%package       -n gem-google-cloud-os-login-v1
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud OS Login V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-os_login-v1) = 0.4.0

%description   -n gem-google-cloud-os-login-v1
Use OS Login to manage SSH access to your instances using IAM without having to
create and manage individual SSH keys. OS Login maintains a consistent Linux
user identity across VM instances and is the recommended way to manage many
users across multiple instances or projects. Note that google-cloud-os_login-v1
is a version-specific client library. For most uses, we recommend installing the
main client library google-cloud-os_login instead. See the readme for more
details.


%package       -n gem-google-cloud-os-login-v1-doc
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud OS Login V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-os_login-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-os_login-v1) = 0.4.0

%description   -n gem-google-cloud-os-login-v1-doc
API Client library for the Cloud OS Login V1 API documentation files.

Use OS Login to manage SSH access to your instances using IAM without having to
create and manage individual SSH keys. OS Login maintains a consistent Linux
user identity across VM instances and is the recommended way to manage many
users across multiple instances or projects. Note that google-cloud-os_login-v1
is a version-specific client library. For most uses, we recommend installing the
main client library google-cloud-os_login instead. See the readme for more
details.

%description   -n gem-google-cloud-os-login-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-os_login-v1.


%package       -n gem-google-cloud-metastore-v1
Version:       0.1.0
Release:       alt1
Summary:       API Client library for the Dataproc Metastore V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-metastore-v1) = 0.1.0

%description   -n gem-google-cloud-metastore-v1
Dataproc Metastore is a fully managed, highly available within a region,
autohealing serverless Apache Hive metastore (HMS) on Google Cloud for data
analytics products. It supports HMS and serves as a critical component for
managing the metadata of relational entities and provides interoperability
between data processing applications in the open source data ecosystem. Note
that google-cloud-metastore-v1 is a version-specific client library. For most
uses, we recommend installing the main client library google-cloud-metastore
instead. See the readme for more details.


%package       -n gem-google-cloud-metastore-v1-doc
Version:       0.1.0
Release:       alt1
Summary:       API Client library for the Dataproc Metastore V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-metastore-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-metastore-v1) = 0.1.0

%description   -n gem-google-cloud-metastore-v1-doc
API Client library for the Dataproc Metastore V1 API documentation
files.

Dataproc Metastore is a fully managed, highly available within a region,
autohealing serverless Apache Hive metastore (HMS) on Google Cloud for data
analytics products. It supports HMS and serves as a critical component for
managing the metadata of relational entities and provides interoperability
between data processing applications in the open source data ecosystem. Note
that google-cloud-metastore-v1 is a version-specific client library. For most
uses, we recommend installing the main client library google-cloud-metastore
instead. See the readme for more details.

%description   -n gem-google-cloud-metastore-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-metastore-v1.


%package       -n gem-google-cloud-dataproc
Version:       1.2.0
Release:       alt1
Summary:       API Client library for the Cloud Dataproc API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-dataproc-v1) >= 0.0 gem(google-cloud-dataproc-v1) < 1
Requires:      gem(google-cloud-dataproc-v1beta2) >= 0.0 gem(google-cloud-dataproc-v1beta2) < 1
Provides:      gem(google-cloud-dataproc) = 1.2.0

%description   -n gem-google-cloud-dataproc
Manages Hadoop-based clusters and jobs on Google Cloud Platform.


%package       -n gem-google-cloud-dataproc-doc
Version:       1.2.0
Release:       alt1
Summary:       API Client library for the Cloud Dataproc API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-dataproc
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-dataproc) = 1.2.0

%description   -n gem-google-cloud-dataproc-doc
API Client library for the Cloud Dataproc API documentation files.

Manages Hadoop-based clusters and jobs on Google Cloud Platform.

%description   -n gem-google-cloud-dataproc-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-dataproc.


%package       -n gem-google-cloud-memcache
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Google Cloud Memorystore for Memcached API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-memcache-v1) >= 0.0 gem(google-cloud-memcache-v1) < 1
Requires:      gem(google-cloud-memcache-v1beta2) >= 0.0 gem(google-cloud-memcache-v1beta2) < 1
Provides:      gem(google-cloud-memcache) = 1.1.0

%description   -n gem-google-cloud-memcache
Google Cloud Memorystore for Memcached API is used for creating and managing
Memcached instances in GCP.


%package       -n gem-google-cloud-memcache-doc
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Google Cloud Memorystore for Memcached API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-memcache
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-memcache) = 1.1.0

%description   -n gem-google-cloud-memcache-doc
API Client library for the Google Cloud Memorystore for Memcached API
documentation files.

Google Cloud Memorystore for Memcached API is used for creating and managing
Memcached instances in GCP.

%description   -n gem-google-cloud-memcache-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-memcache.


%package       -n gem-google-cloud-secret-manager-v1
Version:       0.10.0
Release:       alt1
Summary:       API Client library for the Secret Manager V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Requires:      gem(grpc-google-iam-v1) >= 0.6.10 gem(grpc-google-iam-v1) < 2.0
Provides:      gem(google-cloud-secret_manager-v1) = 0.10.0

%description   -n gem-google-cloud-secret-manager-v1
Secret Manager is a secure and convenient storage system for API keys,
passwords, certificates, and other sensitive data. Secret Manager provides a
central place and single source of truth to manage, access, and audit secrets
across Google Cloud. Note that google-cloud-secret_manager-v1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-secret_manager instead. See the readme for more
details.


%package       -n gem-google-cloud-secret-manager-v1-doc
Version:       0.10.0
Release:       alt1
Summary:       API Client library for the Secret Manager V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-secret_manager-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-secret_manager-v1) = 0.10.0

%description   -n gem-google-cloud-secret-manager-v1-doc
API Client library for the Secret Manager V1 API documentation files.

Secret Manager is a secure and convenient storage system for API keys,
passwords, certificates, and other sensitive data. Secret Manager provides a
central place and single source of truth to manage, access, and audit secrets
across Google Cloud. Note that google-cloud-secret_manager-v1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-secret_manager instead. See the readme for more
details.

%description   -n gem-google-cloud-secret-manager-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-secret_manager-v1.


%package       -n gem-google-cloud-recaptcha-enterprise
Version:       1.2.0
Release:       alt1
Summary:       API Client library for the reCAPTCHA Enterprise API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-recaptcha_enterprise-v1) >= 0.0 gem(google-cloud-recaptcha_enterprise-v1) < 1
Requires:      gem(google-cloud-recaptcha_enterprise-v1beta1) >= 0.0 gem(google-cloud-recaptcha_enterprise-v1beta1) < 1
Provides:      gem(google-cloud-recaptcha_enterprise) = 1.2.0

%description   -n gem-google-cloud-recaptcha-enterprise
reCAPTCHA Enterprise is a service that protects your site from spam and abuse.


%package       -n gem-google-cloud-recaptcha-enterprise-doc
Version:       1.2.0
Release:       alt1
Summary:       API Client library for the reCAPTCHA Enterprise API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-recaptcha_enterprise
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-recaptcha_enterprise) = 1.2.0

%description   -n gem-google-cloud-recaptcha-enterprise-doc
API Client library for the reCAPTCHA Enterprise API documentation
files.

reCAPTCHA Enterprise is a service that protects your site from spam and abuse.

%description   -n gem-google-cloud-recaptcha-enterprise-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-recaptcha_enterprise.


%package       -n gem-stackdriver
Version:       0.21.1
Release:       alt1
Summary:       API Client library for Google Stackdriver
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-error_reporting) >= 0.41 gem(google-cloud-error_reporting) < 1
Requires:      gem(google-cloud-logging) >= 2.1 gem(google-cloud-logging) < 3
Requires:      gem(google-cloud-trace) >= 0.40 gem(google-cloud-trace) < 1
Provides:      gem(stackdriver) = 0.21.1

%description   -n gem-stackdriver
stackdriver is the official library for Google Stackdriver APIs.


%package       -n stackdriver-doc
Version:       0.21.1
Release:       alt1
Summary:       API Client library for Google Stackdriver documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета stackdriver
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(stackdriver) = 0.21.1

%description   -n stackdriver-doc
API Client library for Google Stackdriver documentation files.

stackdriver is the official library for Google Stackdriver APIs.

%description   -n stackdriver-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета stackdriver.


%package       -n gem-google-cloud-bigquery-connection
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the BigQuery Connection API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-bigquery-connection-v1) >= 0.0 gem(google-cloud-bigquery-connection-v1) < 1
Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Provides:      gem(google-cloud-bigquery-connection) = 1.1.0

%description   -n gem-google-cloud-bigquery-connection
The BigQuery Connection API allows users to manage BigQuery connections to
external data sources.


%package       -n gem-google-cloud-bigquery-connection-doc
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the BigQuery Connection API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-bigquery-connection
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-bigquery-connection) = 1.1.0

%description   -n gem-google-cloud-bigquery-connection-doc
API Client library for the BigQuery Connection API documentation files.

The BigQuery Connection API allows users to manage BigQuery connections to
external data sources.

%description   -n gem-google-cloud-bigquery-connection-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-bigquery-connection.


%package       -n gem-google-cloud-dataqna
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the BigQuery Data QnA API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-dataqna-v1alpha) >= 0.0 gem(google-cloud-dataqna-v1alpha) < 1
Provides:      gem(google-cloud-dataqna) = 0.2.0

%description   -n gem-google-cloud-dataqna
Data QnA is a natural language question and answer service for BigQuery data.


%package       -n gem-google-cloud-dataqna-doc
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the BigQuery Data QnA API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-dataqna
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-dataqna) = 0.2.0

%description   -n gem-google-cloud-dataqna-doc
API Client library for the BigQuery Data QnA API documentation files.

Data QnA is a natural language question and answer service for BigQuery data.

%description   -n gem-google-cloud-dataqna-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-dataqna.


%package       -n gem-google-cloud-media-translation
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Media Translation API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-media_translation-v1beta1) >= 0.0 gem(google-cloud-media_translation-v1beta1) < 1
Provides:      gem(google-cloud-media_translation) = 0.2.0

%description   -n gem-google-cloud-media-translation
Media Translation API delivers real-time speech translation to your content and
applications directly from your audio data. Leveraging Google's machine learning
technologies, the API offers enhanced accuracy and simplified integration while
equipping you with a comprehensive set of features to further refine your
translation results. Improve user experience with low-latency streaming
translation and scale quickly with straightforward internationalization.


%package       -n gem-google-cloud-media-translation-doc
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Media Translation API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-media_translation
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-media_translation) = 0.2.0

%description   -n gem-google-cloud-media-translation-doc
API Client library for the Media Translation API documentation files.

Media Translation API delivers real-time speech translation to your content and
applications directly from your audio data. Leveraging Google's machine learning
technologies, the API offers enhanced accuracy and simplified integration while
equipping you with a comprehensive set of features to further refine your
translation results. Improve user experience with low-latency streaming
translation and scale quickly with straightforward internationalization.

%description   -n gem-google-cloud-media-translation-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-media_translation.


%package       -n gem-google-cloud-phishing-protection
Version:       0.11.0
Release:       alt1
Summary:       API Client library for the Phishing Protection API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-phishing_protection-v1beta1) >= 0.0 gem(google-cloud-phishing_protection-v1beta1) < 1
Provides:      gem(google-cloud-phishing_protection) = 0.11.0

%description   -n gem-google-cloud-phishing-protection
Phishing Protection helps prevent users from accessing phishing sites by
identifying various signals associated with malicious content, including the use
of your brand assets, classifying malicious content that uses your brand and
reporting the unsafe URLs to Google Safe Browsing.


%package       -n gem-google-cloud-phishing-protection-doc
Version:       0.11.0
Release:       alt1
Summary:       API Client library for the Phishing Protection API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-phishing_protection
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-phishing_protection) = 0.11.0

%description   -n gem-google-cloud-phishing-protection-doc
API Client library for the Phishing Protection API documentation
files.

Phishing Protection helps prevent users from accessing phishing sites by
identifying various signals associated with malicious content, including the use
of your brand assets, classifying malicious content that uses your brand and
reporting the unsafe URLs to Google Safe Browsing.

%description   -n gem-google-cloud-phishing-protection-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-phishing_protection.


%package       -n gem-google-cloud-memcache-v1
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Google Cloud Memorystore for Memcached V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-memcache-v1) = 0.2.0

%description   -n gem-google-cloud-memcache-v1
Google Cloud Memorystore for Memcached API is used for creating and managing
Memcached instances in GCP. Note that google-cloud-memcache-v1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-memcache instead. See the readme for more details.


%package       -n gem-google-cloud-memcache-v1-doc
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Google Cloud Memorystore for Memcached V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-memcache-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-memcache-v1) = 0.2.0

%description   -n gem-google-cloud-memcache-v1-doc
API Client library for the Google Cloud Memorystore for Memcached V1 API
documentation files.

Google Cloud Memorystore for Memcached API is used for creating and managing
Memcached instances in GCP. Note that google-cloud-memcache-v1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-memcache instead. See the readme for more details.

%description   -n gem-google-cloud-memcache-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-memcache-v1.


%package       -n gem-google-cloud-memcache-v1beta2
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Google Cloud Memorystore for Memcached API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-memcache-v1beta2) = 0.2.0

%description   -n gem-google-cloud-memcache-v1beta2
Google Cloud Memorystore for Memcached API is used for creating and managing
Memcached instances in GCP. Note that google-cloud-memcache-v1beta2 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-memcache instead. See the readme for more details.


%package       -n gem-google-cloud-memcache-v1beta2-doc
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Google Cloud Memorystore for Memcached API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-memcache-v1beta2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-memcache-v1beta2) = 0.2.0

%description   -n gem-google-cloud-memcache-v1beta2-doc
API Client library for the Google Cloud Memorystore for Memcached API
documentation files.

Google Cloud Memorystore for Memcached API is used for creating and managing
Memcached instances in GCP. Note that google-cloud-memcache-v1beta2 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-memcache instead. See the readme for more details.

%description   -n gem-google-cloud-memcache-v1beta2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-memcache-v1beta2.


%package       -n gem-google-cloud-binary-authorization
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Binary Authorization API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-binary_authorization-v1beta1) >= 0.0 gem(google-cloud-binary_authorization-v1beta1) < 1
Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Provides:      gem(google-cloud-binary_authorization) = 0.2.0

%description   -n gem-google-cloud-binary-authorization
Binary Authorization is a service on Google Cloud that provides centralized
software supply-chain security for applications that run on Google Kubernetes
Engine (GKE) and GKE on-prem.


%package       -n gem-google-cloud-binary-authorization-doc
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Binary Authorization API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-binary_authorization
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-binary_authorization) = 0.2.0

%description   -n gem-google-cloud-binary-authorization-doc
API Client library for the Binary Authorization API documentation files.

Binary Authorization is a service on Google Cloud that provides centralized
software supply-chain security for applications that run on Google Kubernetes
Engine (GKE) and GKE on-prem.

%description   -n gem-google-cloud-binary-authorization-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-binary_authorization.


%package       -n gem-stackdriver-core
Version:       1.5.0
Release:       alt1
Summary:       Internal shared library for Ruby Stackdriver integration
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.2 gem(google-cloud-core) < 2
Provides:      gem(stackdriver-core) = 1.5.0

%description   -n gem-stackdriver-core
stackdriver-core is an internal shared library for the Ruby Stackdriver
integration libraries.


%package       -n stackdriver-core-doc
Version:       1.5.0
Release:       alt1
Summary:       Internal shared library for Ruby Stackdriver integration documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета stackdriver-core
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(stackdriver-core) = 1.5.0

%description   -n stackdriver-core-doc
Internal shared library for Ruby Stackdriver integration documentation
files.

stackdriver-core is an internal shared library for the Ruby Stackdriver
integration libraries.

%description   -n stackdriver-core-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета stackdriver-core.


%package       -n gem-google-cloud-profiler-v2
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Cloud Profiler V2 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-profiler-v2) = 0.2.0

%description   -n gem-google-cloud-profiler-v2
Cloud Profiler is a statistical, low-overhead profiler that continuously gathers
CPU usage and memory-allocation information from your production applications.
It attributes that information to the application's source code, helping you
identify the parts of the application consuming the most resources, and
otherwise illuminating the performance characteristics of the code. Note that
google-cloud-profiler-v2 is a version-specific client library. For most uses, we
recommend installing the main client library google-cloud-profiler instead. See
the readme for more details.


%package       -n gem-google-cloud-profiler-v2-doc
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Cloud Profiler V2 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-profiler-v2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-profiler-v2) = 0.2.0

%description   -n gem-google-cloud-profiler-v2-doc
API Client library for the Cloud Profiler V2 API documentation files.

Cloud Profiler is a statistical, low-overhead profiler that continuously gathers
CPU usage and memory-allocation information from your production applications.
It attributes that information to the application's source code, helping you
identify the parts of the application consuming the most resources, and
otherwise illuminating the performance characteristics of the code. Note that
google-cloud-profiler-v2 is a version-specific client library. For most uses, we
recommend installing the main client library google-cloud-profiler instead. See
the readme for more details.

%description   -n gem-google-cloud-profiler-v2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-profiler-v2.


%package       -n gem-google-iam-v1beta
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Google IAM V1beta API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-iam-v1beta) = 0.3.0

%description   -n gem-google-iam-v1beta
Pre-release client for the WorkloadIdentityPools service. Note that
google-iam-v1beta is a version-specific client library. For most uses, we
recommend installing the main client library google-iam instead. See the readme
for more details.


%package       -n gem-google-iam-v1beta-doc
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Google IAM V1beta API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-iam-v1beta
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-iam-v1beta) = 0.3.0

%description   -n gem-google-iam-v1beta-doc
API Client library for the Google IAM V1beta API documentation
files.

Pre-release client for the WorkloadIdentityPools service. Note that
google-iam-v1beta is a version-specific client library. For most uses, we
recommend installing the main client library google-iam instead. See the readme
for more details.

%description   -n gem-google-iam-v1beta-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-iam-v1beta.


%package       -n gem-google-cloud-automl-v1
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud AutoML V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-automl-v1) = 0.4.0

%description   -n gem-google-cloud-automl-v1
AutoML makes the power of machine learning available to you even if you have
limited knowledge of machine learning. You can use AutoML to build on Google's
machine learning capabilities to create your own custom machine learning models
that are tailored to your business needs, and then integrate those models into
your applications and web sites. Note that google-cloud-automl-v1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-automl instead. See the readme for more details.


%package       -n gem-google-cloud-automl-v1-doc
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud AutoML V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-automl-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-automl-v1) = 0.4.0

%description   -n gem-google-cloud-automl-v1-doc
API Client library for the Cloud AutoML V1 API documentation files.

AutoML makes the power of machine learning available to you even if you have
limited knowledge of machine learning. You can use AutoML to build on Google's
machine learning capabilities to create your own custom machine learning models
that are tailored to your business needs, and then integrate those models into
your applications and web sites. Note that google-cloud-automl-v1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-automl instead. See the readme for more details.

%description   -n gem-google-cloud-automl-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-automl-v1.


%package       -n gem-google-cloud-billing-v1
Version:       0.7.0
Release:       alt1
Summary:       API Client library for the Billing V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Requires:      gem(grpc-google-iam-v1) >= 0.6.10 gem(grpc-google-iam-v1) < 2.0
Provides:      gem(google-cloud-billing-v1) = 0.7.0

%description   -n gem-google-cloud-billing-v1
Allows developers to manage billing for their Google Cloud Platform projects
programmatically. Note that google-cloud-billing-v1 is a version-specific client
library. For most uses, we recommend installing the main client library
google-cloud-billing instead. See the readme for more details.


%package       -n gem-google-cloud-billing-v1-doc
Version:       0.7.0
Release:       alt1
Summary:       API Client library for the Billing V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-billing-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-billing-v1) = 0.7.0

%description   -n gem-google-cloud-billing-v1-doc
API Client library for the Billing V1 API documentation files.

Allows developers to manage billing for their Google Cloud Platform projects
programmatically. Note that google-cloud-billing-v1 is a version-specific client
library. For most uses, we recommend installing the main client library
google-cloud-billing instead. See the readme for more details.

%description   -n gem-google-cloud-billing-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-billing-v1.


%package       -n gem-google-cloud-os-login
Version:       1.2.0
Release:       alt1
Summary:       API Client library for the Cloud OS Login API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-os_login-v1) >= 0.0 gem(google-cloud-os_login-v1) < 1
Requires:      gem(google-cloud-os_login-v1beta) >= 0.0 gem(google-cloud-os_login-v1beta) < 1
Provides:      gem(google-cloud-os_login) = 1.2.0

%description   -n gem-google-cloud-os-login
Use OS Login to manage SSH access to your instances using IAM without having to
create and manage individual SSH keys. OS Login maintains a consistent Linux
user identity across VM instances and is the recommended way to manage many
users across multiple instances or projects.


%package       -n gem-google-cloud-os-login-doc
Version:       1.2.0
Release:       alt1
Summary:       API Client library for the Cloud OS Login API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-os_login
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-os_login) = 1.2.0

%description   -n gem-google-cloud-os-login-doc
API Client library for the Cloud OS Login API documentation files.

Use OS Login to manage SSH access to your instances using IAM without having to
create and manage individual SSH keys. OS Login maintains a consistent Linux
user identity across VM instances and is the recommended way to manage many
users across multiple instances or projects.

%description   -n gem-google-cloud-os-login-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-os_login.


%package       -n gem-google-cloud-gke-hub
Version:       0.1.0
Release:       alt1
Summary:       API Client library for the GKE Hub API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-gke_hub-v1beta1) >= 0.0 gem(google-cloud-gke_hub-v1beta1) < 1
Provides:      gem(google-cloud-gke_hub) = 0.1.0

%description   -n gem-google-cloud-gke-hub
The GKE Hub API centrally manages features and services on all your Kubernetes
clusters running in a variety of environments, including Google cloud, on
premises in customer datacenters, or other third party clouds.


%package       -n gem-google-cloud-gke-hub-doc
Version:       0.1.0
Release:       alt1
Summary:       API Client library for the GKE Hub API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-gke_hub
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-gke_hub) = 0.1.0

%description   -n gem-google-cloud-gke-hub-doc
API Client library for the GKE Hub API documentation files.

The GKE Hub API centrally manages features and services on all your Kubernetes
clusters running in a variety of environments, including Google cloud, on
premises in customer datacenters, or other third party clouds.

%description   -n gem-google-cloud-gke-hub-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-gke_hub.


%package       -n gem-google-cloud-language-v1beta2
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Natural Language V1beta2 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-language-v1beta2) = 0.4.0

%description   -n gem-google-cloud-language-v1beta2
Provides natural language understanding technologies, such as sentiment
analysis, entity recognition, entity sentiment analysis, and other text
annotations. Note that google-cloud-language-v1beta2 is a version-specific
client library. For most uses, we recommend installing the main client library
google-cloud-language instead. See the readme for more details.


%package       -n gem-google-cloud-language-v1beta2-doc
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Natural Language V1beta2 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-language-v1beta2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-language-v1beta2) = 0.4.0

%description   -n gem-google-cloud-language-v1beta2-doc
API Client library for the Natural Language V1beta2 API documentation
files.

Provides natural language understanding technologies, such as sentiment
analysis, entity recognition, entity sentiment analysis, and other text
annotations. Note that google-cloud-language-v1beta2 is a version-specific
client library. For most uses, we recommend installing the main client library
google-cloud-language instead. See the readme for more details.

%description   -n gem-google-cloud-language-v1beta2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-language-v1beta2.


%package       -n gem-google-cloud-scheduler
Version:       2.2.0
Release:       alt1
Summary:       API Client library for the Cloud Scheduler API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-scheduler-v1) >= 0.0 gem(google-cloud-scheduler-v1) < 1
Requires:      gem(google-cloud-scheduler-v1beta1) >= 0.0 gem(google-cloud-scheduler-v1beta1) < 1
Provides:      gem(google-cloud-scheduler) = 2.2.0

%description   -n gem-google-cloud-scheduler
Cloud Scheduler is a fully managed enterprise-grade cron job scheduler. It
allows you to schedule virtually any job, including batch, big data jobs, cloud
infrastructure operations, and more. You can automate everything, including
retries in case of failure to reduce manual toil and intervention. Cloud
Scheduler even acts as a single pane of glass, allowing you to manage all your
automation tasks from one place.


%package       -n gem-google-cloud-scheduler-doc
Version:       2.2.0
Release:       alt1
Summary:       API Client library for the Cloud Scheduler API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-scheduler
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-scheduler) = 2.2.0

%description   -n gem-google-cloud-scheduler-doc
API Client library for the Cloud Scheduler API documentation files.

Cloud Scheduler is a fully managed enterprise-grade cron job scheduler. It
allows you to schedule virtually any job, including batch, big data jobs, cloud
infrastructure operations, and more. You can automate everything, including
retries in case of failure to reduce manual toil and intervention. Cloud
Scheduler even acts as a single pane of glass, allowing you to manage all your
automation tasks from one place.

%description   -n gem-google-cloud-scheduler-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-scheduler.


%package       -n gem-google-cloud-recaptcha-enterprise-v1
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the reCAPTCHA Enterprise V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-recaptcha_enterprise-v1) = 0.4.0

%description   -n gem-google-cloud-recaptcha-enterprise-v1
reCAPTCHA Enterprise is a service that protects your site from spam and abuse.
Note that google-cloud-recaptcha_enterprise-v1 is a version-specific client
library. For most uses, we recommend installing the main client library
google-cloud-recaptcha_enterprise instead. See the readme for more details.


%package       -n gem-google-cloud-recaptcha-enterprise-v1-doc
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the reCAPTCHA Enterprise V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-recaptcha_enterprise-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-recaptcha_enterprise-v1) = 0.4.0

%description   -n gem-google-cloud-recaptcha-enterprise-v1-doc
API Client library for the reCAPTCHA Enterprise V1 API documentation
files.

reCAPTCHA Enterprise is a service that protects your site from spam and abuse.
Note that google-cloud-recaptcha_enterprise-v1 is a version-specific client
library. For most uses, we recommend installing the main client library
google-cloud-recaptcha_enterprise instead. See the readme for more details.

%description   -n gem-google-cloud-recaptcha-enterprise-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-recaptcha_enterprise-v1.


%package       -n gem-google-cloud-errors
Version:       1.1.0
Release:       alt1
Summary:       Error classes for google-cloud-ruby
Group:         Development/Ruby
BuildArch:     noarch

Provides:      gem(google-cloud-errors) = 1.1.0

%description   -n gem-google-cloud-errors
google-cloud-errors defines error classes for google-cloud-ruby.


%package       -n gem-google-cloud-errors-doc
Version:       1.1.0
Release:       alt1
Summary:       Error classes for google-cloud-ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-errors
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-errors) = 1.1.0

%description   -n gem-google-cloud-errors-doc
Error classes for google-cloud-ruby documentation files.

google-cloud-errors defines error classes for google-cloud-ruby.

%description   -n gem-google-cloud-errors-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-errors.


%package       -n gem-google-cloud-workflows
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Workflows API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-workflows-v1beta) >= 0.0 gem(google-cloud-workflows-v1beta) < 1
Requires:      gem(google-cloud-workflows-executions-v1beta) >= 0.0 gem(google-cloud-workflows-executions-v1beta) < 1
Provides:      gem(google-cloud-workflows) = 1.1.0

%description   -n gem-google-cloud-workflows
Workflows link series of serverless tasks together in an order you define.
Combine the power of Google Cloud's APIs, serverless products like Cloud
Functions and Cloud Run, and calls to external APIs to create flexible
serverless applications. Workflows requires no infrastructure management and
scales seamlessly with demand, including scaling down to zero..


%package       -n gem-google-cloud-workflows-doc
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Workflows API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-workflows
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-workflows) = 1.1.0

%description   -n gem-google-cloud-workflows-doc
API Client library for the Workflows API documentation files.

Workflows link series of serverless tasks together in an order you define.
Combine the power of Google Cloud's APIs, serverless products like Cloud
Functions and Cloud Run, and calls to external APIs to create flexible
serverless applications. Workflows requires no infrastructure management and
scales seamlessly with demand, including scaling down to zero..

%description   -n gem-google-cloud-workflows-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-workflows.


%package       -n gem-google-cloud-trace
Version:       0.41.0
Release:       alt1
Summary:       Application Instrumentation and API Client library for Stackdriver Trace
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(stackdriver-core) >= 1.3 gem(stackdriver-core) < 2
Requires:      gem(concurrent-ruby) >= 1.1 gem(concurrent-ruby) < 2
Requires:      gem(google-cloud-trace-v1) >= 0.0 gem(google-cloud-trace-v1) < 1
Requires:      gem(google-cloud-trace-v2) >= 0.0 gem(google-cloud-trace-v2) < 1
Provides:      gem(google-cloud-trace) = 0.41.0

%description   -n gem-google-cloud-trace
google-cloud-trace is the official library for Stackdriver Trace.


%package       -n gem-google-cloud-trace-doc
Version:       0.41.0
Release:       alt1
Summary:       Application Instrumentation and API Client library for Stackdriver Trace documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-trace
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-trace) = 0.41.0

%description   -n gem-google-cloud-trace-doc
Application Instrumentation and API Client library for Stackdriver Trace
documentation files.

google-cloud-trace is the official library for Stackdriver Trace.

%description   -n gem-google-cloud-trace-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-trace.


%package       -n gem-google-cloud-container-v1
Version:       0.5.0
Release:       alt1
Summary:       API Client library for the Kubernetes Engine V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-container-v1) = 0.5.0

%description   -n gem-google-cloud-container-v1
Builds and manages container-based applications, powered by the open source
Kubernetes technology. Note that google-cloud-container-v1 is a version-specific
client library. For most uses, we recommend installing the main client library
google-cloud-container instead. See the readme for more details.


%package       -n gem-google-cloud-container-v1-doc
Version:       0.5.0
Release:       alt1
Summary:       API Client library for the Kubernetes Engine V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-container-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-container-v1) = 0.5.0

%description   -n gem-google-cloud-container-v1-doc
API Client library for the Kubernetes Engine V1 API documentation files.

Builds and manages container-based applications, powered by the open source
Kubernetes technology. Note that google-cloud-container-v1 is a version-specific
client library. For most uses, we recommend installing the main client library
google-cloud-container instead. See the readme for more details.

%description   -n gem-google-cloud-container-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-container-v1.


%package       -n gem-google-cloud-security-center
Version:       1.2.0
Release:       alt1
Summary:       API Client library for the Security Command Center API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-security_center-v1) >= 0.0 gem(google-cloud-security_center-v1) < 1
Requires:      gem(google-cloud-security_center-v1p1beta1) >= 0.0 gem(google-cloud-security_center-v1p1beta1) < 1
Provides:      gem(google-cloud-security_center) = 1.2.0

%description   -n gem-google-cloud-security-center
Security Command Center API provides access to temporal views of assets and
findings within an organization.


%package       -n gem-google-cloud-security-center-doc
Version:       1.2.0
Release:       alt1
Summary:       API Client library for the Security Command Center API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-security_center
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-security_center) = 1.2.0

%description   -n gem-google-cloud-security-center-doc
API Client library for the Security Command Center API documentation
files.

Security Command Center API provides access to temporal views of assets and
findings within an organization.

%description   -n gem-google-cloud-security-center-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-security_center.


%package       -n gem-google-cloud-recommendation-engine-v1beta1
Version:       0.3.1
Release:       alt1
Summary:       API Client library for the Recommendations AI V1beta1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-recommendation_engine-v1beta1) = 0.3.1

%description   -n gem-google-cloud-recommendation-engine-v1beta1
Recommendations AI enables you to build an end-to-end personalized
recommendation system based on state-of-the-art deep learning ML models, without
a need for expertise in ML or recommendation systems. Note that
google-cloud-recommendation_engine-v1beta1 is a version-specific client library.
For most uses, we recommend installing the main client library
google-cloud-recommendation_engine instead. See the readme for more details.


%package       -n gem-google-cloud-recommendation-engine-v1beta1-doc
Version:       0.3.1
Release:       alt1
Summary:       API Client library for the Recommendations AI V1beta1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-recommendation_engine-v1beta1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-recommendation_engine-v1beta1) = 0.3.1

%description   -n gem-google-cloud-recommendation-engine-v1beta1-doc
API Client library for the Recommendations AI V1beta1 API documentation
files.

Recommendations AI enables you to build an end-to-end personalized
recommendation system based on state-of-the-art deep learning ML models, without
a need for expertise in ML or recommendation systems. Note that
google-cloud-recommendation_engine-v1beta1 is a version-specific client library.
For most uses, we recommend installing the main client library
google-cloud-recommendation_engine instead. See the readme for more details.

%description   -n gem-google-cloud-recommendation-engine-v1beta1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-recommendation_engine-v1beta1.


%package       -n gem-google-cloud-assured-workloads
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Assured Workloads for Government API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-assured_workloads-v1beta1) >= 0.0 gem(google-cloud-assured_workloads-v1beta1) < 1
Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Provides:      gem(google-cloud-assured_workloads) = 0.2.0

%description   -n gem-google-cloud-assured-workloads
Assured Workloads for Government secures government workloads and accelerates
the path to running compliant workloads on Google Cloud.


%package       -n gem-google-cloud-assured-workloads-doc
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Assured Workloads for Government API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-assured_workloads
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-assured_workloads) = 0.2.0

%description   -n gem-google-cloud-assured-workloads-doc
API Client library for the Assured Workloads for Government API documentation
files.

Assured Workloads for Government secures government workloads and accelerates
the path to running compliant workloads on Google Cloud.

%description   -n gem-google-cloud-assured-workloads-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-assured_workloads.


%package       -n gem-google-cloud-web-security-scanner
Version:       1.0.0
Release:       alt1
Summary:       API Client library for the Web Security Scanner API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-web_security_scanner-v1) >= 0.3 gem(google-cloud-web_security_scanner-v1) < 1
Requires:      gem(google-cloud-web_security_scanner-v1beta) >= 0.3 gem(google-cloud-web_security_scanner-v1beta) < 1
Provides:      gem(google-cloud-web_security_scanner) = 1.0.0

%description   -n gem-google-cloud-web-security-scanner
Web Security Scanner scans your Compute and App Engine apps for common web
vulnerabilities.


%package       -n gem-google-cloud-web-security-scanner-doc
Version:       1.0.0
Release:       alt1
Summary:       API Client library for the Web Security Scanner API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-web_security_scanner
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-web_security_scanner) = 1.0.0

%description   -n gem-google-cloud-web-security-scanner-doc
API Client library for the Web Security Scanner API documentation files.

Web Security Scanner scans your Compute and App Engine apps for common web
vulnerabilities.

%description   -n gem-google-cloud-web-security-scanner-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-web_security_scanner.


%package       -n gem-google-cloud-text-to-speech
Version:       1.2.0
Release:       alt1
Summary:       API Client library for the Cloud Text-to-Speech API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-text_to_speech-v1) >= 0.0 gem(google-cloud-text_to_speech-v1) < 1
Requires:      gem(google-cloud-text_to_speech-v1beta1) >= 0.0 gem(google-cloud-text_to_speech-v1beta1) < 1
Provides:      gem(google-cloud-text_to_speech) = 1.2.0

%description   -n gem-google-cloud-text-to-speech
Text-to-Speech converts text or Speech Synthesis Markup Language (SSML) input
into audio data of natural human speech.


%package       -n gem-google-cloud-text-to-speech-doc
Version:       1.2.0
Release:       alt1
Summary:       API Client library for the Cloud Text-to-Speech API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-text_to_speech
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-text_to_speech) = 1.2.0

%description   -n gem-google-cloud-text-to-speech-doc
API Client library for the Cloud Text-to-Speech API documentation
files.

Text-to-Speech converts text or Speech Synthesis Markup Language (SSML) input
into audio data of natural human speech.

%description   -n gem-google-cloud-text-to-speech-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-text_to_speech.


%package       -n gem-google-cloud-org-policy
Version:       1.0.0
Release:       alt1
Summary:       API Client library for the Organization Policy API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-org_policy-v2) >= 0.2 gem(google-cloud-org_policy-v2) < 1
Provides:      gem(google-cloud-org_policy) = 1.0.0

%description   -n gem-google-cloud-org-policy
The Cloud Org Policy service provides a simple mechanism for organizations to
restrict the allowed configurations across their entire Cloud Resource
hierarchy.


%package       -n gem-google-cloud-org-policy-doc
Version:       1.0.0
Release:       alt1
Summary:       API Client library for the Organization Policy API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-org_policy
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-org_policy) = 1.0.0

%description   -n gem-google-cloud-org-policy-doc
API Client library for the Organization Policy API documentation files.

The Cloud Org Policy service provides a simple mechanism for organizations to
restrict the allowed configurations across their entire Cloud Resource
hierarchy.

%description   -n gem-google-cloud-org-policy-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-org_policy.


%package       -n gem-google-cloud-firestore-admin-v1
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Cloud Firestore Admin V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-firestore-admin-v1) = 0.3.0

%description   -n gem-google-cloud-firestore-admin-v1
Cloud Firestore is a NoSQL document database built for automatic scaling, high
performance, and ease of application development. Note that
google-cloud-firestore-admin-v1 is a version-specific client library. For most
uses, we recommend installing the main client library
google-cloud-firestore-admin instead. See the readme for more details.


%package       -n gem-google-cloud-firestore-admin-v1-doc
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Cloud Firestore Admin V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-firestore-admin-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-firestore-admin-v1) = 0.3.0

%description   -n gem-google-cloud-firestore-admin-v1-doc
API Client library for the Cloud Firestore Admin V1 API documentation
files.

Cloud Firestore is a NoSQL document database built for automatic scaling, high
performance, and ease of application development. Note that
google-cloud-firestore-admin-v1 is a version-specific client library. For most
uses, we recommend installing the main client library
google-cloud-firestore-admin instead. See the readme for more details.

%description   -n gem-google-cloud-firestore-admin-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-firestore-admin-v1.


%package       -n gem-google-cloud-dns
Version:       0.35.0
Release:       alt1
Summary:       API Client library for Google Cloud DNS
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.2 gem(google-cloud-core) < 2
Requires:      gem(google-apis-dns_v1) >= 0.1 gem(google-apis-dns_v1) < 1
Requires:      gem(googleauth) >= 0.9 gem(googleauth) < 1
Requires:      gem(zonefile) >= 1.04 gem(zonefile) < 2
Provides:      gem(google-cloud-dns) = 0.35.0

%description   -n gem-google-cloud-dns
google-cloud-dns is the official library for Google Cloud DNS.


%package       -n gem-google-cloud-dns-doc
Version:       0.35.0
Release:       alt1
Summary:       API Client library for Google Cloud DNS documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-dns
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-dns) = 0.35.0

%description   -n gem-google-cloud-dns-doc
API Client library for Google Cloud DNS documentation files.

google-cloud-dns is the official library for Google Cloud DNS.

%description   -n gem-google-cloud-dns-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-dns.


%package       -n gem-google-cloud-video-intelligence-v1
Version:       0.6.0
Release:       alt1
Summary:       API Client library for the Cloud Video Intelligence V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-video_intelligence-v1) = 0.6.0

%description   -n gem-google-cloud-video-intelligence-v1
Detects objects, explicit content, and scene changes in videos. It also
specifies the region for annotation and transcribes speech to text. Supports
both asynchronous API and streaming API. Note that
google-cloud-video_intelligence-v1 is a version-specific client library. For
most uses, we recommend installing the main client library
google-cloud-video_intelligence instead. See the readme for more details.


%package       -n gem-google-cloud-video-intelligence-v1-doc
Version:       0.6.0
Release:       alt1
Summary:       API Client library for the Cloud Video Intelligence V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-video_intelligence-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-video_intelligence-v1) = 0.6.0

%description   -n gem-google-cloud-video-intelligence-v1-doc
API Client library for the Cloud Video Intelligence V1 API documentation
files.

Detects objects, explicit content, and scene changes in videos. It also
specifies the region for annotation and transcribes speech to text. Supports
both asynchronous API and streaming API. Note that
google-cloud-video_intelligence-v1 is a version-specific client library. For
most uses, we recommend installing the main client library
google-cloud-video_intelligence instead. See the readme for more details.

%description   -n gem-google-cloud-video-intelligence-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-video_intelligence-v1.


%package       -n gem-google-cloud-assured-workloads-v1beta1
Version:       0.6.0
Release:       alt1
Summary:       API Client library for the Assured Workloads for Government V1beta1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-assured_workloads-v1beta1) = 0.6.0

%description   -n gem-google-cloud-assured-workloads-v1beta1
Assured Workloads for Government secures government workloads and accelerates
the path to running compliant workloads on Google Cloud. Note that
google-cloud-assured_workloads-v1beta1 is a version-specific client library. For
most uses, we recommend installing the main client library
google-cloud-assured_workloads instead. See the readme for more details.


%package       -n gem-google-cloud-assured-workloads-v1beta1-doc
Version:       0.6.0
Release:       alt1
Summary:       API Client library for the Assured Workloads for Government V1beta1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-assured_workloads-v1beta1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-assured_workloads-v1beta1) = 0.6.0

%description   -n gem-google-cloud-assured-workloads-v1beta1-doc
API Client library for the Assured Workloads for Government V1beta1 API
documentation files.

Assured Workloads for Government secures government workloads and accelerates
the path to running compliant workloads on Google Cloud. Note that
google-cloud-assured_workloads-v1beta1 is a version-specific client library. For
most uses, we recommend installing the main client library
google-cloud-assured_workloads instead. See the readme for more details.

%description   -n gem-google-cloud-assured-workloads-v1beta1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-assured_workloads-v1beta1.


%package       -n gem-google-cloud-language
Version:       1.3.0
Release:       alt1
Summary:       API Client library for the Cloud Natural Language API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-language-v1) >= 0.1 gem(google-cloud-language-v1) < 1
Requires:      gem(google-cloud-language-v1beta2) >= 0.1 gem(google-cloud-language-v1beta2) < 1
Provides:      gem(google-cloud-language) = 1.3.0

%description   -n gem-google-cloud-language
Provides natural language understanding technologies, such as sentiment
analysis, entity recognition, entity sentiment analysis, and other text
annotations.


%package       -n gem-google-cloud-language-doc
Version:       1.3.0
Release:       alt1
Summary:       API Client library for the Cloud Natural Language API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-language
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-language) = 1.3.0

%description   -n gem-google-cloud-language-doc
API Client library for the Cloud Natural Language API documentation
files.

Provides natural language understanding technologies, such as sentiment
analysis, entity recognition, entity sentiment analysis, and other text
annotations.

%description   -n gem-google-cloud-language-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-language.


%package       -n gem-google-cloud-container
Version:       1.2.0
Release:       alt1
Summary:       API Client library for the Kubernetes Engine API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-container-v1) >= 0.0 gem(google-cloud-container-v1) < 1
Requires:      gem(google-cloud-container-v1beta1) >= 0.0 gem(google-cloud-container-v1beta1) < 1
Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Provides:      gem(google-cloud-container) = 1.2.0

%description   -n gem-google-cloud-container
Builds and manages container-based applications, powered by the open source
Kubernetes technology.


%package       -n gem-google-cloud-container-doc
Version:       1.2.0
Release:       alt1
Summary:       API Client library for the Kubernetes Engine API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-container
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-container) = 1.2.0

%description   -n gem-google-cloud-container-doc
API Client library for the Kubernetes Engine API documentation files.

Builds and manages container-based applications, powered by the open source
Kubernetes technology.

%description   -n gem-google-cloud-container-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-container.


%package       -n gem-google-cloud-compute-v1
Version:       0.1.0
Release:       alt1
Summary:       API Client library (ALPHA) for the Google Cloud Compute V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4.1 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-compute-v1) = 0.1.0

%description   -n gem-google-cloud-compute-v1
google-cloud-compute-v1 is the official client library for the Google Cloud
Compute V1 API. This library is considered to be in alpha. This means it is
still a work-in-progress and under active development. Any release is subject to
backwards-incompatible changes at any time.


%package       -n gem-google-cloud-compute-v1-doc
Version:       0.1.0
Release:       alt1
Summary:       API Client library (ALPHA) for the Google Cloud Compute V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-compute-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-compute-v1) = 0.1.0

%description   -n gem-google-cloud-compute-v1-doc
API Client library (ALPHA) for the Google Cloud Compute V1 API documentation
files.

google-cloud-compute-v1 is the official client library for the Google Cloud
Compute V1 API. This library is considered to be in alpha. This means it is
still a work-in-progress and under active development. Any release is subject to
backwards-incompatible changes at any time.

%description   -n gem-google-cloud-compute-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-compute-v1.


%package       -n gem-google-cloud-artifact-registry-v1beta2
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Artifact Registry V1beta2 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Requires:      gem(grpc-google-iam-v1) >= 0.6.10 gem(grpc-google-iam-v1) < 2.0
Provides:      gem(google-cloud-artifact_registry-v1beta2) = 0.3.0

%description   -n gem-google-cloud-artifact-registry-v1beta2
Artifact Registry stores and manages build artifacts in a scalable and
integrated service built on Google infrastructure. Note that
google-cloud-artifact_registry-v1beta2 is a version-specific client library. For
most uses, we recommend installing the main client library
google-cloud-artifact_registry instead. See the readme for more details.


%package       -n gem-google-cloud-artifact-registry-v1beta2-doc
Version:       0.3.0
Release:       alt1
Summary:       API Client library for the Artifact Registry V1beta2 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-artifact_registry-v1beta2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-artifact_registry-v1beta2) = 0.3.0

%description   -n gem-google-cloud-artifact-registry-v1beta2-doc
API Client library for the Artifact Registry V1beta2 API documentation
files.

Artifact Registry stores and manages build artifacts in a scalable and
integrated service built on Google infrastructure. Note that
google-cloud-artifact_registry-v1beta2 is a version-specific client library. For
most uses, we recommend installing the main client library
google-cloud-artifact_registry instead. See the readme for more details.

%description   -n gem-google-cloud-artifact-registry-v1beta2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-artifact_registry-v1beta2.


%package       -n gem-google-cloud-container-v1beta1
Version:       0.5.1
Release:       alt1
Summary:       API Client library for the Kubernetes Engine V1beta1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-container-v1beta1) = 0.5.1

%description   -n gem-google-cloud-container-v1beta1
Builds and manages container-based applications, powered by the open source
Kubernetes technology. Note that google-cloud-container-v1beta1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-container instead. See the readme for more details.


%package       -n gem-google-cloud-container-v1beta1-doc
Version:       0.5.1
Release:       alt1
Summary:       API Client library for the Kubernetes Engine V1beta1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-container-v1beta1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-container-v1beta1) = 0.5.1

%description   -n gem-google-cloud-container-v1beta1-doc
API Client library for the Kubernetes Engine V1beta1 API documentation
files.

Builds and manages container-based applications, powered by the open source
Kubernetes technology. Note that google-cloud-container-v1beta1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-container instead. See the readme for more details.

%description   -n gem-google-cloud-container-v1beta1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-container-v1beta1.


%package       -n gem-google-cloud-web-risk
Version:       1.2.0
Release:       alt1
Summary:       API Client library for the Web Risk API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-web_risk-v1) >= 0.0 gem(google-cloud-web_risk-v1) < 1
Requires:      gem(google-cloud-web_risk-v1beta1) >= 0.0 gem(google-cloud-web_risk-v1beta1) < 1
Provides:      gem(google-cloud-web_risk) = 1.2.0

%description   -n gem-google-cloud-web-risk
Web Risk is an enterprise security product that lets your client applications
check URLs against Google's constantly updated lists of unsafe web resources.


%package       -n gem-google-cloud-web-risk-doc
Version:       1.2.0
Release:       alt1
Summary:       API Client library for the Web Risk API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-web_risk
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-web_risk) = 1.2.0

%description   -n gem-google-cloud-web-risk-doc
API Client library for the Web Risk API documentation files.

Web Risk is an enterprise security product that lets your client applications
check URLs against Google's constantly updated lists of unsafe web resources.

%description   -n gem-google-cloud-web-risk-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-web_risk.


%package       -n gem-google-cloud-logging
Version:       2.2.0
Release:       alt1
Summary:       API Client library for Stackdriver Logging
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-logging-v2) >= 0.0 gem(google-cloud-logging-v2) < 1
Requires:      gem(stackdriver-core) >= 1.3 gem(stackdriver-core) < 2
Requires:      gem(concurrent-ruby) >= 1.1 gem(concurrent-ruby) < 2
Provides:      gem(google-cloud-logging) = 2.2.0

%description   -n gem-google-cloud-logging
google-cloud-logging is the official library for Stackdriver Logging.


%package       -n gem-google-cloud-logging-doc
Version:       2.2.0
Release:       alt1
Summary:       API Client library for Stackdriver Logging documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-logging
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-logging) = 2.2.0

%description   -n gem-google-cloud-logging-doc
API Client library for Stackdriver Logging documentation
files.

google-cloud-logging is the official library for Stackdriver Logging.

%description   -n gem-google-cloud-logging-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-logging.


%package       -n gem-google-cloud-security-private-ca
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Certificate Authority Service API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-security-private_ca-v1beta1) >= 0.0 gem(google-cloud-security-private_ca-v1beta1) < 1
Provides:      gem(google-cloud-security-private_ca) = 0.2.0

%description   -n gem-google-cloud-security-private-ca
Certificate Authority Service is a highly available, scalable Google Cloud
service that enables you to simplify, automate, and customize the deployment,
management, and security of private certificate authorities (CA).


%package       -n gem-google-cloud-security-private-ca-doc
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Certificate Authority Service API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-security-private_ca
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-security-private_ca) = 0.2.0

%description   -n gem-google-cloud-security-private-ca-doc
API Client library for the Certificate Authority Service API documentation
files.

Certificate Authority Service is a highly available, scalable Google Cloud
service that enables you to simplify, automate, and customize the deployment,
management, and security of private certificate authorities (CA).

%description   -n gem-google-cloud-security-private-ca-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-security-private_ca.


%package       -n gem-google-cloud-domains
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Cloud Domains API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-domains-v1beta1) >= 0.0 gem(google-cloud-domains-v1beta1) < 1
Provides:      gem(google-cloud-domains) = 0.2.0

%description   -n gem-google-cloud-domains
The Cloud Domains API provides registration, management and configuration of
domain names.


%package       -n gem-google-cloud-domains-doc
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Cloud Domains API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-domains
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-domains) = 0.2.0

%description   -n gem-google-cloud-domains-doc
API Client library for the Cloud Domains API documentation files.

The Cloud Domains API provides registration, management and configuration of
domain names.

%description   -n gem-google-cloud-domains-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-domains.


%package       -n gem-google-cloud-pubsub-v1
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud Pub/Sub V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Requires:      gem(grpc-google-iam-v1) >= 0.6.10 gem(grpc-google-iam-v1) < 2.0
Provides:      gem(google-cloud-pubsub-v1) = 0.4.0

%description   -n gem-google-cloud-pubsub-v1
Cloud Pub/Sub is a fully-managed real-time messaging service that allows you to
send and receive messages between independent applications. Note that
google-cloud-pubsub-v1 is a version-specific client library. For most uses, we
recommend installing the main client library google-cloud-pubsub instead. See
the readme for more details.


%package       -n gem-google-cloud-pubsub-v1-doc
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Cloud Pub/Sub V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-pubsub-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-pubsub-v1) = 0.4.0

%description   -n gem-google-cloud-pubsub-v1-doc
API Client library for the Cloud Pub/Sub V1 API documentation files.

Cloud Pub/Sub is a fully-managed real-time messaging service that allows you to
send and receive messages between independent applications. Note that
google-cloud-pubsub-v1 is a version-specific client library. For most uses, we
recommend installing the main client library google-cloud-pubsub instead. See
the readme for more details.

%description   -n gem-google-cloud-pubsub-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-pubsub-v1.


%package       -n gem-google-cloud-dlp-v2
Version:       0.7.0
Release:       alt1
Summary:       API Client library for the Cloud Data Loss Prevention (DLP) V2 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-dlp-v2) = 0.7.0

%description   -n gem-google-cloud-dlp-v2
Provides methods for detection of privacy-sensitive fragments in text, images,
and Google Cloud Platform storage repositories. Note that google-cloud-dlp-v2 is
a version-specific client library. For most uses, we recommend installing the
main client library google-cloud-dlp instead. See the readme for more details.


%package       -n gem-google-cloud-dlp-v2-doc
Version:       0.7.0
Release:       alt1
Summary:       API Client library for the Cloud Data Loss Prevention (DLP) V2 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-dlp-v2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-dlp-v2) = 0.7.0

%description   -n gem-google-cloud-dlp-v2-doc
API Client library for the Cloud Data Loss Prevention (DLP) V2 API documentation
files.

Provides methods for detection of privacy-sensitive fragments in text, images,
and Google Cloud Platform storage repositories. Note that google-cloud-dlp-v2 is
a version-specific client library. For most uses, we recommend installing the
main client library google-cloud-dlp instead. See the readme for more details.

%description   -n gem-google-cloud-dlp-v2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-dlp-v2.


%package       -n gem-google-cloud-security-center-v1p1beta1
Version:       0.7.0
Release:       alt1
Summary:       API Client library for the Cloud Security Command Center V1p1beta1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Requires:      gem(grpc-google-iam-v1) >= 0.6.10 gem(grpc-google-iam-v1) < 2.0
Provides:      gem(google-cloud-security_center-v1p1beta1) = 0.7.0

%description   -n gem-google-cloud-security-center-v1p1beta1
Security Command Center API provides access to temporal views of assets and
findings within an organization. Note that
google-cloud-security_center-v1p1beta1 is a version-specific client library. For
most uses, we recommend installing the main client library
google-cloud-security_center instead. See the readme for more details.


%package       -n gem-google-cloud-security-center-v1p1beta1-doc
Version:       0.7.0
Release:       alt1
Summary:       API Client library for the Cloud Security Command Center V1p1beta1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-security_center-v1p1beta1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-security_center-v1p1beta1) = 0.7.0

%description   -n gem-google-cloud-security-center-v1p1beta1-doc
API Client library for the Cloud Security Command Center V1p1beta1 API
documentation files.

Security Command Center API provides access to temporal views of assets and
findings within an organization. Note that
google-cloud-security_center-v1p1beta1 is a version-specific client library. For
most uses, we recommend installing the main client library
google-cloud-security_center instead. See the readme for more details.

%description   -n gem-google-cloud-security-center-v1p1beta1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-security_center-v1p1beta1.


%package       -n gem-google-cloud-dataproc-v1beta2
Version:       0.6.0
Release:       alt1
Summary:       API Client library for the Cloud Dataproc V1beta2 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-dataproc-v1beta2) = 0.6.0

%description   -n gem-google-cloud-dataproc-v1beta2
Manages Hadoop-based clusters and jobs on Google Cloud Platform. Note that
google-cloud-dataproc-v1beta2 is a version-specific client library. For most
uses, we recommend installing the main client library google-cloud-dataproc
instead. See the readme for more details.


%package       -n gem-google-cloud-dataproc-v1beta2-doc
Version:       0.6.0
Release:       alt1
Summary:       API Client library for the Cloud Dataproc V1beta2 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-dataproc-v1beta2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-dataproc-v1beta2) = 0.6.0

%description   -n gem-google-cloud-dataproc-v1beta2-doc
API Client library for the Cloud Dataproc V1beta2 API documentation
files.

Manages Hadoop-based clusters and jobs on Google Cloud Platform. Note that
google-cloud-dataproc-v1beta2 is a version-specific client library. For most
uses, we recommend installing the main client library google-cloud-dataproc
instead. See the readme for more details.

%description   -n gem-google-cloud-dataproc-v1beta2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-dataproc-v1beta2.


%package       -n gem-google-cloud-web-risk-v1beta1
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Web Risk V1beta1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-web_risk-v1beta1) = 0.4.0

%description   -n gem-google-cloud-web-risk-v1beta1
Web Risk is an enterprise security product that lets your client applications
check URLs against Google's constantly updated lists of unsafe web resources.
Note that google-cloud-web_risk-v1beta1 is a version-specific client library.
For most uses, we recommend installing the main client library
google-cloud-web_risk instead. See the readme for more details.


%package       -n gem-google-cloud-web-risk-v1beta1-doc
Version:       0.4.0
Release:       alt1
Summary:       API Client library for the Web Risk V1beta1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-web_risk-v1beta1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-web_risk-v1beta1) = 0.4.0

%description   -n gem-google-cloud-web-risk-v1beta1-doc
API Client library for the Web Risk V1beta1 API documentation files.

Web Risk is an enterprise security product that lets your client applications
check URLs against Google's constantly updated lists of unsafe web resources.
Note that google-cloud-web_risk-v1beta1 is a version-specific client library.
For most uses, we recommend installing the main client library
google-cloud-web_risk instead. See the readme for more details.

%description   -n gem-google-cloud-web-risk-v1beta1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-web_risk-v1beta1.


%package       -n gem-grafeas-v1
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Grafeas V1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(grafeas-v1) = 0.2.0

%description   -n gem-grafeas-v1
The Grafeas API stores, and enables querying and retrieval of, critical metadata
about all of your software artifacts. Note that grafeas-v1 is a version-specific
client library. For most uses, we recommend installing the main client library
grafeas instead. See the readme for more details.


%package       -n grafeas-v1-doc
Version:       0.2.0
Release:       alt1
Summary:       API Client library for the Grafeas V1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета grafeas-v1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(grafeas-v1) = 0.2.0

%description   -n grafeas-v1-doc
API Client library for the Grafeas V1 API documentation files.

The Grafeas API stores, and enables querying and retrieval of, critical metadata
about all of your software artifacts. Note that grafeas-v1 is a version-specific
client library. For most uses, we recommend installing the main client library
grafeas instead. See the readme for more details.

%description   -n grafeas-v1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета grafeas-v1.


%package       -n gem-google-cloud-automl-v1beta1
Version:       0.5.0
Release:       alt1
Summary:       API Client library for the Cloud AutoML V1beta1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-automl-v1beta1) = 0.5.0

%description   -n gem-google-cloud-automl-v1beta1
AutoML makes the power of machine learning available to you even if you have
limited knowledge of machine learning. You can use AutoML to build on Google's
machine learning capabilities to create your own custom machine learning models
that are tailored to your business needs, and then integrate those models into
your applications and web sites. Note that google-cloud-automl-v1beta1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-automl instead. See the readme for more details.


%package       -n gem-google-cloud-automl-v1beta1-doc
Version:       0.5.0
Release:       alt1
Summary:       API Client library for the Cloud AutoML V1beta1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-automl-v1beta1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-automl-v1beta1) = 0.5.0

%description   -n gem-google-cloud-automl-v1beta1-doc
API Client library for the Cloud AutoML V1beta1 API documentation files.

AutoML makes the power of machine learning available to you even if you have
limited knowledge of machine learning. You can use AutoML to build on Google's
machine learning capabilities to create your own custom machine learning models
that are tailored to your business needs, and then integrate those models into
your applications and web sites. Note that google-cloud-automl-v1beta1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-automl instead. See the readme for more details.

%description   -n gem-google-cloud-automl-v1beta1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-automl-v1beta1.


%package       -n gem-google-cloud-secret-manager-v1beta1
Version:       0.8.0
Release:       alt1
Summary:       API Client library for the Secret Manager V1beta1 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Requires:      gem(grpc-google-iam-v1) >= 0.6.10 gem(grpc-google-iam-v1) < 2.0
Provides:      gem(google-cloud-secret_manager-v1beta1) = 0.8.0

%description   -n gem-google-cloud-secret-manager-v1beta1
Secret Manager is a secure and convenient storage system for API keys,
passwords, certificates, and other sensitive data. Secret Manager provides a
central place and single source of truth to manage, access, and audit secrets
across Google Cloud. Note that google-cloud-secret_manager-v1beta1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-secret_manager instead. See the readme for more
details.


%package       -n gem-google-cloud-secret-manager-v1beta1-doc
Version:       0.8.0
Release:       alt1
Summary:       API Client library for the Secret Manager V1beta1 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-secret_manager-v1beta1
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-secret_manager-v1beta1) = 0.8.0

%description   -n gem-google-cloud-secret-manager-v1beta1-doc
API Client library for the Secret Manager V1beta1 API documentation
files.

Secret Manager is a secure and convenient storage system for API keys,
passwords, certificates, and other sensitive data. Secret Manager provides a
central place and single source of truth to manage, access, and audit secrets
across Google Cloud. Note that google-cloud-secret_manager-v1beta1 is a
version-specific client library. For most uses, we recommend installing the main
client library google-cloud-secret_manager instead. See the readme for more
details.

%description   -n gem-google-cloud-secret-manager-v1beta1-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-secret_manager-v1beta1.


%package       -n gem-google-cloud-managed-identities
Version:       1.0.0
Release:       alt1
Summary:       API Client library for the Managed Service for Microsoft Active Directory API API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Requires:      gem(google-cloud-managed_identities-v1) >= 0.3 gem(google-cloud-managed_identities-v1) < 1
Provides:      gem(google-cloud-managed_identities) = 1.0.0

%description   -n gem-google-cloud-managed-identities
The Managed Service for Microsoft Active Directory API is used for managing a
highly available, hardened service running Microsoft Active Directory.


%package       -n gem-google-cloud-managed-identities-doc
Version:       1.0.0
Release:       alt1
Summary:       API Client library for the Managed Service for Microsoft Active Directory API API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-managed_identities
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-managed_identities) = 1.0.0

%description   -n gem-google-cloud-managed-identities-doc
API Client library for the Managed Service for Microsoft Active Directory API
API documentation files.

The Managed Service for Microsoft Active Directory API is used for managing a
highly available, hardened service running Microsoft Active Directory.

%description   -n gem-google-cloud-managed-identities-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-managed_identities.


%package       -n gem-google-cloud-billing-budgets
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Billing Budgets API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-billing-budgets-v1beta1) >= 0.0 gem(google-cloud-billing-budgets-v1beta1) < 1
Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Provides:      gem(google-cloud-billing-budgets) = 1.1.0

%description   -n gem-google-cloud-billing-budgets
Provides methods to view, create, and manage Cloud Billing budgets
programmatically at scale.


%package       -n gem-google-cloud-billing-budgets-doc
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Billing Budgets API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-billing-budgets
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-billing-budgets) = 1.1.0

%description   -n gem-google-cloud-billing-budgets-doc
API Client library for the Billing Budgets API documentation files.

Provides methods to view, create, and manage Cloud Billing budgets
programmatically at scale.

%description   -n gem-google-cloud-billing-budgets-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-billing-budgets.


%package       -n gem-google-cloud-automl
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Cloud AutoML API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(google-cloud-automl-v1) >= 0.0 gem(google-cloud-automl-v1) < 1
Requires:      gem(google-cloud-automl-v1beta1) >= 0.0 gem(google-cloud-automl-v1beta1) < 1
Requires:      gem(google-cloud-core) >= 1.5 gem(google-cloud-core) < 2
Provides:      gem(google-cloud-automl) = 1.1.0

%description   -n gem-google-cloud-automl
AutoML makes the power of machine learning available to you even if you have
limited knowledge of machine learning. You can use AutoML to build on Google's
machine learning capabilities to create your own custom machine learning models
that are tailored to your business needs, and then integrate those models into
your applications and web sites.


%package       -n gem-google-cloud-automl-doc
Version:       1.1.0
Release:       alt1
Summary:       API Client library for the Cloud AutoML API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-automl
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-automl) = 1.1.0

%description   -n gem-google-cloud-automl-doc
API Client library for the Cloud AutoML API documentation files.

AutoML makes the power of machine learning available to you even if you have
limited knowledge of machine learning. You can use AutoML to build on Google's
machine learning capabilities to create your own custom machine learning models
that are tailored to your business needs, and then integrate those models into
your applications and web sites.

%description   -n gem-google-cloud-automl-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-automl.


%package       -n gem-google-cloud-document-ai-v1beta3
Version:       0.9.0
Release:       alt1
Summary:       API Client library for the Document AI V1beta3 API
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gapic-common) >= 0.4 gem(gapic-common) < 1
Requires:      gem(google-cloud-errors) >= 1.0 gem(google-cloud-errors) < 2
Provides:      gem(google-cloud-document_ai-v1beta3) = 0.9.0

%description   -n gem-google-cloud-document-ai-v1beta3
Document AI uses machine learning on a single cloud-based platform to
automatically classify, extract, and enrich data within your documents to unlock
insights. Note that google-cloud-document_ai-v1beta3 is a version-specific
client library. For most uses, we recommend installing the main client library
google-cloud-document_ai instead. See the readme for more details.


%package       -n gem-google-cloud-document-ai-v1beta3-doc
Version:       0.9.0
Release:       alt1
Summary:       API Client library for the Document AI V1beta3 API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета google-cloud-document_ai-v1beta3
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(google-cloud-document_ai-v1beta3) = 0.9.0

%description   -n gem-google-cloud-document-ai-v1beta3-doc
API Client library for the Document AI V1beta3 API documentation
files.

Document AI uses machine learning on a single cloud-based platform to
automatically classify, extract, and enrich data within your documents to unlock
insights. Note that google-cloud-document_ai-v1beta3 is a version-specific
client library. For most uses, we recommend installing the main client library
google-cloud-document_ai instead. See the readme for more details.

%description   -n gem-google-cloud-document-ai-v1beta3-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета google-cloud-document_ai-v1beta3.


%prep
%setup
%patch

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files

%files         -n gem-google-cloud-channel-v1
%doc README.md
%ruby_gemspecdir/google-cloud-channel-v1-0.6.0.gemspec
%ruby_gemslibdir/google-cloud-channel-v1-0.6.0

%files         -n gem-google-cloud-channel-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-channel-v1-0.6.0

%files         -n gem-google-cloud-bigquery-data-transfer-v1
%doc README.md
%ruby_gemspecdir/google-cloud-bigquery-data_transfer-v1-0.4.0.gemspec
%ruby_gemslibdir/google-cloud-bigquery-data_transfer-v1-0.4.0

%files         -n gem-google-cloud-bigquery-data-transfer-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-bigquery-data_transfer-v1-0.4.0

%files         -n gem-google-cloud-core
%doc README.md
%ruby_gemspecdir/google-cloud-core-1.6.0.gemspec
%ruby_gemslibdir/google-cloud-core-1.6.0

%files         -n gem-google-cloud-core-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-core-1.6.0

%files         -n gem-google-cloud-workflows-v1beta
%doc README.md
%ruby_gemspecdir/google-cloud-workflows-v1beta-0.3.0.gemspec
%ruby_gemslibdir/google-cloud-workflows-v1beta-0.3.0

%files         -n gem-google-cloud-workflows-v1beta-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-workflows-v1beta-0.3.0

%files         -n gem-google-cloud-scheduler-v1beta1
%doc README.md
%ruby_gemspecdir/google-cloud-scheduler-v1beta1-0.4.0.gemspec
%ruby_gemslibdir/google-cloud-scheduler-v1beta1-0.4.0

%files         -n gem-google-cloud-scheduler-v1beta1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-scheduler-v1beta1-0.4.0

%files         -n gem-google-cloud-bigquery-connection-v1
%doc README.md
%ruby_gemspecdir/google-cloud-bigquery-connection-v1-0.4.0.gemspec
%ruby_gemslibdir/google-cloud-bigquery-connection-v1-0.4.0

%files         -n gem-google-cloud-bigquery-connection-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-bigquery-connection-v1-0.4.0

%files         -n gem-google-cloud-tasks-v2beta3
%doc README.md
%ruby_gemspecdir/google-cloud-tasks-v2beta3-0.6.0.gemspec
%ruby_gemslibdir/google-cloud-tasks-v2beta3-0.6.0

%files         -n gem-google-cloud-tasks-v2beta3-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-tasks-v2beta3-0.6.0

%files         -n gem-google-area120-tables-v1alpha1
%doc README.md
%ruby_gemspecdir/google-area120-tables-v1alpha1-0.2.0.gemspec
%ruby_gemslibdir/google-area120-tables-v1alpha1-0.2.0

%files         -n gem-google-area120-tables-v1alpha1-doc
%doc README.md
%ruby_gemsdocdir/google-area120-tables-v1alpha1-0.2.0

%files         -n gem-google-cloud-speech
%doc README.md
%ruby_gemspecdir/google-cloud-speech-1.2.0.gemspec
%ruby_gemslibdir/google-cloud-speech-1.2.0

%files         -n gem-google-cloud-speech-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-speech-1.2.0

%files         -n gem-google-cloud-trace-v2
%doc README.md
%ruby_gemspecdir/google-cloud-trace-v2-0.3.0.gemspec
%ruby_gemslibdir/google-cloud-trace-v2-0.3.0

%files         -n gem-google-cloud-trace-v2-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-trace-v2-0.3.0

%files         -n gem-google-cloud-service-directory
%doc README.md
%ruby_gemspecdir/google-cloud-service_directory-1.1.0.gemspec
%ruby_gemslibdir/google-cloud-service_directory-1.1.0

%files         -n gem-google-cloud-service-directory-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-service_directory-1.1.0

%files         -n gem-google-cloud-vision-v1
%doc README.md
%ruby_gemspecdir/google-cloud-vision-v1-0.6.0.gemspec
%ruby_gemslibdir/google-cloud-vision-v1-0.6.0

%files         -n gem-google-cloud-vision-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-vision-v1-0.6.0

%files         -n gem-google-cloud-workflows-executions-v1beta
%doc README.md
%ruby_gemspecdir/google-cloud-workflows-executions-v1beta-0.3.0.gemspec
%ruby_gemslibdir/google-cloud-workflows-executions-v1beta-0.3.0

%files         -n gem-google-cloud-workflows-executions-v1beta-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-workflows-executions-v1beta-0.3.0

%files         -n gem-google-cloud-datastore-admin-v1
%doc README.md
%ruby_gemspecdir/google-cloud-datastore-admin-v1-0.4.0.gemspec
%ruby_gemslibdir/google-cloud-datastore-admin-v1-0.4.0

%files         -n gem-google-cloud-datastore-admin-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-datastore-admin-v1-0.4.0

%files         -n gem-google-cloud-org-policy-v2
%doc README.md
%ruby_gemspecdir/google-cloud-org_policy-v2-0.2.0.gemspec
%ruby_gemslibdir/google-cloud-org_policy-v2-0.2.0

%files         -n gem-google-cloud-org-policy-v2-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-org_policy-v2-0.2.0

%files         -n gem-google-cloud-service-management
%doc README.md
%ruby_gemspecdir/google-cloud-service_management-1.0.1.gemspec
%ruby_gemslibdir/google-cloud-service_management-1.0.1

%files         -n gem-google-cloud-service-management-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-service_management-1.0.1

%files         -n gem-google-cloud-spanner-v1
%doc README.md
%ruby_gemspecdir/google-cloud-spanner-v1-0.6.1.gemspec
%ruby_gemslibdir/google-cloud-spanner-v1-0.6.1

%files         -n gem-google-cloud-spanner-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-spanner-v1-0.6.1

%files         -n gem-google-cloud-access-approval-v1
%doc README.md
%ruby_gemspecdir/google-cloud-access_approval-v1-0.4.0.gemspec
%ruby_gemslibdir/google-cloud-access_approval-v1-0.4.0

%files         -n gem-google-cloud-access-approval-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-access_approval-v1-0.4.0

%files         -n gem-google-cloud-firestore
%ruby_gemspecdir/google-cloud-firestore-2.5.1.gemspec
%ruby_gemslibdir/google-cloud-firestore-2.5.1

%files         -n gem-google-cloud-firestore-doc
%ruby_gemsdocdir/google-cloud-firestore-2.5.1

%files         -n gem-google-cloud-talent-v4
%doc README.md
%ruby_gemspecdir/google-cloud-talent-v4-0.4.0.gemspec
%ruby_gemslibdir/google-cloud-talent-v4-0.4.0

%files         -n gem-google-cloud-talent-v4-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-talent-v4-0.4.0

%files         -n gem-google-cloud-data-labeling-v1beta1
%doc README.md
%ruby_gemspecdir/google-cloud-data_labeling-v1beta1-0.3.0.gemspec
%ruby_gemslibdir/google-cloud-data_labeling-v1beta1-0.3.0

%files         -n gem-google-cloud-data-labeling-v1beta1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-data_labeling-v1beta1-0.3.0

%files         -n gem-google-cloud-bigquery-reservation-v1
%doc README.md
%ruby_gemspecdir/google-cloud-bigquery-reservation-v1-0.3.0.gemspec
%ruby_gemslibdir/google-cloud-bigquery-reservation-v1-0.3.0

%files         -n gem-google-cloud-bigquery-reservation-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-bigquery-reservation-v1-0.3.0

%files         -n gem-google-cloud-artifact-registry
%doc README.md
%ruby_gemspecdir/google-cloud-artifact_registry-0.2.0.gemspec
%ruby_gemslibdir/google-cloud-artifact_registry-0.2.0

%files         -n gem-google-cloud-artifact-registry-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-artifact_registry-0.2.0

%files         -n gem-google-cloud-kms
%doc README.md
%ruby_gemspecdir/google-cloud-kms-2.1.0.gemspec
%ruby_gemslibdir/google-cloud-kms-2.1.0

%files         -n gem-google-cloud-kms-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-kms-2.1.0

%files         -n gem-google-cloud-container-analysis
%doc README.md
%ruby_gemspecdir/google-cloud-container_analysis-1.1.0.gemspec
%ruby_gemslibdir/google-cloud-container_analysis-1.1.0

%files         -n gem-google-cloud-container-analysis-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-container_analysis-1.1.0

%files         -n gem-google-iam-credentials
%doc README.md
%ruby_gemspecdir/google-iam-credentials-1.0.0.gemspec
%ruby_gemslibdir/google-iam-credentials-1.0.0

%files         -n gem-google-iam-credentials-doc
%doc README.md
%ruby_gemsdocdir/google-iam-credentials-1.0.0

%files         -n gem-google-cloud-talent-v4beta1
%doc README.md
%ruby_gemspecdir/google-cloud-talent-v4beta1-0.4.0.gemspec
%ruby_gemslibdir/google-cloud-talent-v4beta1-0.4.0

%files         -n gem-google-cloud-talent-v4beta1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-talent-v4beta1-0.4.0

%files         -n gem-google-cloud-vision
%doc README.md
%ruby_gemspecdir/google-cloud-vision-1.1.0.gemspec
%ruby_gemslibdir/google-cloud-vision-1.1.0

%files         -n gem-google-cloud-vision-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-vision-1.1.0

%files         -n gem-google-cloud-translate-v2
%doc README.md
%ruby_gemspecdir/google-cloud-translate-v2-0.3.0.gemspec
%ruby_gemslibdir/google-cloud-translate-v2-0.3.0

%files         -n gem-google-cloud-translate-v2-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-translate-v2-0.3.0

%files         -n gem-google-cloud-resource-manager
%ruby_gemspecdir/google-cloud-resource_manager-0.36.0.gemspec
%ruby_gemslibdir/google-cloud-resource_manager-0.36.0

%files         -n gem-google-cloud-resource-manager-doc
%ruby_gemsdocdir/google-cloud-resource_manager-0.36.0

%files         -n gem-google-cloud-data-labeling
%doc README.md
%ruby_gemspecdir/google-cloud-data_labeling-0.2.0.gemspec
%ruby_gemslibdir/google-cloud-data_labeling-0.2.0

%files         -n gem-google-cloud-data-labeling-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-data_labeling-0.2.0

%files         -n gem-google-cloud-bigquery-storage-v1
%doc README.md
%ruby_gemspecdir/google-cloud-bigquery-storage-v1-0.6.0.gemspec
%ruby_gemslibdir/google-cloud-bigquery-storage-v1-0.6.0

%files         -n gem-google-cloud-bigquery-storage-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-bigquery-storage-v1-0.6.0

%files         -n gem-google-cloud-policy-troubleshooter-v1
%doc README.md
%ruby_gemspecdir/google-cloud-policy_troubleshooter-v1-0.3.0.gemspec
%ruby_gemslibdir/google-cloud-policy_troubleshooter-v1-0.3.0

%files         -n gem-google-cloud-policy-troubleshooter-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-policy_troubleshooter-v1-0.3.0

%files         -n gem-google-cloud-managed-identities-v1
%doc README.md
%ruby_gemspecdir/google-cloud-managed_identities-v1-0.3.0.gemspec
%ruby_gemslibdir/google-cloud-managed_identities-v1-0.3.0

%files         -n gem-google-cloud-managed-identities-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-managed_identities-v1-0.3.0

%files         -n gem-google-cloud-bigquery-storage
%doc README.md
%ruby_gemspecdir/google-cloud-bigquery-storage-1.1.0.gemspec
%ruby_gemslibdir/google-cloud-bigquery-storage-1.1.0

%files         -n gem-google-cloud-bigquery-storage-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-bigquery-storage-1.1.0

%files         -n gem-google-cloud-video-transcoder-v1beta1
%doc README.md
%ruby_gemspecdir/google-cloud-video-transcoder-v1beta1-0.2.0.gemspec
%ruby_gemslibdir/google-cloud-video-transcoder-v1beta1-0.2.0

%files         -n gem-google-cloud-video-transcoder-v1beta1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-video-transcoder-v1beta1-0.2.0

%files         -n gem-google-cloud-binary-authorization-v1beta1
%doc README.md
%ruby_gemspecdir/google-cloud-binary_authorization-v1beta1-0.3.0.gemspec
%ruby_gemslibdir/google-cloud-binary_authorization-v1beta1-0.3.0

%files         -n gem-google-cloud-binary-authorization-v1beta1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-binary_authorization-v1beta1-0.3.0

%files         -n gem-google-cloud-recommender-v1
%doc README.md
%ruby_gemspecdir/google-cloud-recommender-v1-0.8.0.gemspec
%ruby_gemslibdir/google-cloud-recommender-v1-0.8.0

%files         -n gem-google-cloud-recommender-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-recommender-v1-0.8.0

%files         -n gem-google-cloud-bigquery-reservation
%doc README.md
%ruby_gemspecdir/google-cloud-bigquery-reservation-1.1.0.gemspec
%ruby_gemslibdir/google-cloud-bigquery-reservation-1.1.0

%files         -n gem-google-cloud-bigquery-reservation-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-bigquery-reservation-1.1.0

%files         -n gem-google-cloud-gaming-v1
%doc README.md
%ruby_gemspecdir/google-cloud-gaming-v1-0.3.0.gemspec
%ruby_gemslibdir/google-cloud-gaming-v1-0.3.0

%files         -n gem-google-cloud-gaming-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-gaming-v1-0.3.0

%files         -n gem-google-cloud-dialogflow
%doc README.md
%ruby_gemspecdir/google-cloud-dialogflow-1.3.0.gemspec
%ruby_gemslibdir/google-cloud-dialogflow-1.3.0

%files         -n gem-google-cloud-dialogflow-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-dialogflow-1.3.0

%files         -n gem-google-cloud-spanner-admin-instance-v1
%doc README.md
%ruby_gemspecdir/google-cloud-spanner-admin-instance-v1-0.3.1.gemspec
%ruby_gemslibdir/google-cloud-spanner-admin-instance-v1-0.3.1

%files         -n gem-google-cloud-spanner-admin-instance-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-spanner-admin-instance-v1-0.3.1

%files         -n gem-google-cloud-webrisk
%doc README.md
%ruby_gemspecdir/google-cloud-webrisk-0.6.0.gemspec
%ruby_gemslibdir/google-cloud-webrisk-0.6.0

%files         -n gem-google-cloud-webrisk-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-webrisk-0.6.0

%files         -n gem-google-cloud-monitoring-dashboard-v1
%doc README.md
%ruby_gemspecdir/google-cloud-monitoring-dashboard-v1-0.5.0.gemspec
%ruby_gemslibdir/google-cloud-monitoring-dashboard-v1-0.5.0

%files         -n gem-google-cloud-monitoring-dashboard-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-monitoring-dashboard-v1-0.5.0

%files         -n gem-google-cloud-error-reporting-v1beta1
%doc README.md
%ruby_gemspecdir/google-cloud-error_reporting-v1beta1-0.4.0.gemspec
%ruby_gemslibdir/google-cloud-error_reporting-v1beta1-0.4.0

%files         -n gem-google-cloud-error-reporting-v1beta1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-error_reporting-v1beta1-0.4.0

%files         -n gem-google-cloud-video-intelligence-v1p2beta1
%doc README.md
%ruby_gemspecdir/google-cloud-video_intelligence-v1p2beta1-0.4.0.gemspec
%ruby_gemslibdir/google-cloud-video_intelligence-v1p2beta1-0.4.0

%files         -n gem-google-cloud-video-intelligence-v1p2beta1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-video_intelligence-v1p2beta1-0.4.0

%files         -n gem-google-analytics-admin-v1alpha
%doc README.md
%ruby_gemspecdir/google-analytics-admin-v1alpha-0.7.0.gemspec
%ruby_gemslibdir/google-analytics-admin-v1alpha-0.7.0

%files         -n gem-google-analytics-admin-v1alpha-doc
%doc README.md
%ruby_gemsdocdir/google-analytics-admin-v1alpha-0.7.0

%files         -n gem-google-cloud-gaming
%doc README.md
%ruby_gemspecdir/google-cloud-gaming-1.1.0.gemspec
%ruby_gemslibdir/google-cloud-gaming-1.1.0

%files         -n gem-google-cloud-gaming-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-gaming-1.1.0

%files         -n gem-google-cloud-service-management-v1
%doc README.md
%ruby_gemspecdir/google-cloud-service_management-v1-0.3.1.gemspec
%ruby_gemslibdir/google-cloud-service_management-v1-0.3.1

%files         -n gem-google-cloud-service-management-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-service_management-v1-0.3.1

%files         -n gem-google-cloud-build
%doc README.md
%ruby_gemspecdir/google-cloud-build-1.1.0.gemspec
%ruby_gemslibdir/google-cloud-build-1.1.0

%files         -n gem-google-cloud-build-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-build-1.1.0

%files         -n gem-google-cloud-tasks-v2beta2
%doc README.md
%ruby_gemspecdir/google-cloud-tasks-v2beta2-0.5.0.gemspec
%ruby_gemslibdir/google-cloud-tasks-v2beta2-0.5.0

%files         -n gem-google-cloud-tasks-v2beta2-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-tasks-v2beta2-0.5.0

%files         -n gem-google-cloud-retail-v2
%doc README.md
%ruby_gemspecdir/google-cloud-retail-v2-0.3.0.gemspec
%ruby_gemslibdir/google-cloud-retail-v2-0.3.0

%files         -n gem-google-cloud-retail-v2-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-retail-v2-0.3.0

%files         -n gem-google-cloud-spanner-admin-database-v1
%doc README.md
%ruby_gemspecdir/google-cloud-spanner-admin-database-v1-0.6.0.gemspec
%ruby_gemslibdir/google-cloud-spanner-admin-database-v1-0.6.0

%files         -n gem-google-cloud-spanner-admin-database-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-spanner-admin-database-v1-0.6.0

%files         -n gem-google-cloud-functions
%doc README.md
%ruby_gemspecdir/google-cloud-functions-1.1.0.gemspec
%ruby_gemslibdir/google-cloud-functions-1.1.0

%files         -n gem-google-cloud-functions-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-functions-1.1.0

%files         -n gem-google-cloud-dataproc-v1
%doc README.md
%ruby_gemspecdir/google-cloud-dataproc-v1-0.6.0.gemspec
%ruby_gemslibdir/google-cloud-dataproc-v1-0.6.0

%files         -n gem-google-cloud-dataproc-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-dataproc-v1-0.6.0

%files         -n gem-google-cloud-security-center-v1
%doc README.md
%ruby_gemspecdir/google-cloud-security_center-v1-0.7.0.gemspec
%ruby_gemslibdir/google-cloud-security_center-v1-0.7.0

%files         -n gem-google-cloud-security-center-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-security_center-v1-0.7.0

%files         -n gem-google-cloud-video-intelligence-v1p1beta1
%doc README.md
%ruby_gemspecdir/google-cloud-video_intelligence-v1p1beta1-0.4.0.gemspec
%ruby_gemslibdir/google-cloud-video_intelligence-v1p1beta1-0.4.0

%files         -n gem-google-cloud-video-intelligence-v1p1beta1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-video_intelligence-v1p1beta1-0.4.0

%files         -n gem-google-cloud-web-security-scanner-v1
%doc README.md
%ruby_gemspecdir/google-cloud-web_security_scanner-v1-0.3.0.gemspec
%ruby_gemslibdir/google-cloud-web_security_scanner-v1-0.3.0

%files         -n gem-google-cloud-web-security-scanner-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-web_security_scanner-v1-0.3.0

%files         -n gem-google-cloud-error-reporting
%ruby_gemspecdir/google-cloud-error_reporting-0.42.0.gemspec
%ruby_gemslibdir/google-cloud-error_reporting-0.42.0

%files         -n gem-google-cloud-error-reporting-doc
%ruby_gemsdocdir/google-cloud-error_reporting-0.42.0

%files         -n gem-google-cloud-asset-v1
%doc README.md
%ruby_gemspecdir/google-cloud-asset-v1-0.11.0.gemspec
%ruby_gemslibdir/google-cloud-asset-v1-0.11.0

%files         -n gem-google-cloud-asset-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-asset-v1-0.11.0

%files         -n gem-google-cloud-api-gateway
%doc README.md
%ruby_gemspecdir/google-cloud-api_gateway-0.1.0.gemspec
%ruby_gemslibdir/google-cloud-api_gateway-0.1.0

%files         -n gem-google-cloud-api-gateway-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-api_gateway-0.1.0

%files         -n gem-google-cloud-notebooks-v1beta1
%doc README.md
%ruby_gemspecdir/google-cloud-notebooks-v1beta1-0.4.0.gemspec
%ruby_gemslibdir/google-cloud-notebooks-v1beta1-0.4.0

%files         -n gem-google-cloud-notebooks-v1beta1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-notebooks-v1beta1-0.4.0

%files         -n gem-google-cloud-tasks
%doc README.md
%ruby_gemspecdir/google-cloud-tasks-2.2.0.gemspec
%ruby_gemslibdir/google-cloud-tasks-2.2.0

%files         -n gem-google-cloud-tasks-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-tasks-2.2.0

%files         -n gem-google-cloud-metastore
%doc README.md
%ruby_gemspecdir/google-cloud-metastore-0.1.0.gemspec
%ruby_gemslibdir/google-cloud-metastore-0.1.0

%files         -n gem-google-cloud-metastore-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-metastore-0.1.0

%files         -n gem-google-cloud-dlp
%doc README.md
%ruby_gemspecdir/google-cloud-dlp-1.2.0.gemspec
%ruby_gemslibdir/google-cloud-dlp-1.2.0

%files         -n gem-google-cloud-dlp-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-dlp-1.2.0

%files         -n gem-grafeas-client
%doc README.md
%ruby_gemspecdir/grafeas-client-0.4.0.gemspec
%ruby_gemslibdir/grafeas-client-0.4.0

%files         -n grafeas-client-doc
%doc README.md
%ruby_gemsdocdir/grafeas-client-0.4.0

%files         -n gem-google-cloud-data-catalog
%doc README.md
%ruby_gemspecdir/google-cloud-data_catalog-1.2.0.gemspec
%ruby_gemslibdir/google-cloud-data_catalog-1.2.0

%files         -n gem-google-cloud-data-catalog-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-data_catalog-1.2.0

%files         -n gem-google-cloud-billing-budgets-v1beta1
%doc README.md
%ruby_gemspecdir/google-cloud-billing-budgets-v1beta1-0.6.0.gemspec
%ruby_gemslibdir/google-cloud-billing-budgets-v1beta1-0.6.0

%files         -n gem-google-cloud-billing-budgets-v1beta1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-billing-budgets-v1beta1-0.6.0

%files         -n gem-google-cloud-profiler
%doc README.md
%ruby_gemspecdir/google-cloud-profiler-1.0.0.gemspec
%ruby_gemslibdir/google-cloud-profiler-1.0.0

%files         -n gem-google-cloud-profiler-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-profiler-1.0.0

%files         -n gem-google-cloud-functions-v1
%doc README.md
%ruby_gemspecdir/google-cloud-functions-v1-0.3.0.gemspec
%ruby_gemslibdir/google-cloud-functions-v1-0.3.0

%files         -n gem-google-cloud-functions-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-functions-v1-0.3.0

%files         -n gem-google-cloud-debugger-v2
%doc README.md
%ruby_gemspecdir/google-cloud-debugger-v2-0.3.0.gemspec
%ruby_gemslibdir/google-cloud-debugger-v2-0.3.0

%files         -n gem-google-cloud-debugger-v2-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-debugger-v2-0.3.0

%files         -n gem-google-cloud-domains-v1beta1
%doc README.md
%ruby_gemspecdir/google-cloud-domains-v1beta1-0.2.0.gemspec
%ruby_gemslibdir/google-cloud-domains-v1beta1-0.2.0

%files         -n gem-google-cloud-domains-v1beta1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-domains-v1beta1-0.2.0

%files         -n gem-google-cloud-monitoring-v3
%doc README.md
%ruby_gemspecdir/google-cloud-monitoring-v3-0.4.0.gemspec
%ruby_gemslibdir/google-cloud-monitoring-v3-0.4.0

%files         -n gem-google-cloud-monitoring-v3-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-monitoring-v3-0.4.0

%files         -n gem-google-cloud-monitoring
%doc README.md
%ruby_gemspecdir/google-cloud-monitoring-1.2.0.gemspec
%ruby_gemslibdir/google-cloud-monitoring-1.2.0

%files         -n gem-google-cloud-monitoring-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-monitoring-1.2.0

%files         -n gem-google-cloud-recommender
%doc README.md
%ruby_gemspecdir/google-cloud-recommender-1.1.0.gemspec
%ruby_gemslibdir/google-cloud-recommender-1.1.0

%files         -n gem-google-cloud-recommender-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-recommender-1.1.0

%files         -n gem-google-cloud-speech-v1
%doc README.md
%ruby_gemspecdir/google-cloud-speech-v1-0.4.0.gemspec
%ruby_gemslibdir/google-cloud-speech-v1-0.4.0

%files         -n gem-google-cloud-speech-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-speech-v1-0.4.0

%files         -n gem-google-cloud-metastore-v1beta
%doc README.md
%ruby_gemspecdir/google-cloud-metastore-v1beta-0.1.0.gemspec
%ruby_gemslibdir/google-cloud-metastore-v1beta-0.1.0

%files         -n gem-google-cloud-metastore-v1beta-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-metastore-v1beta-0.1.0

%files         -n gem-google-cloud-datastore-v1
%doc README.md
%ruby_gemspecdir/google-cloud-datastore-v1-0.3.0.gemspec
%ruby_gemslibdir/google-cloud-datastore-v1-0.3.0

%files         -n gem-google-cloud-datastore-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-datastore-v1-0.3.0

%files         -n gem-google-cloud-secret-manager
%doc README.md
%ruby_gemspecdir/google-cloud-secret_manager-1.1.0.gemspec
%ruby_gemslibdir/google-cloud-secret_manager-1.1.0

%files         -n gem-google-cloud-secret-manager-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-secret_manager-1.1.0

%files         -n gem-google-cloud-network-connectivity-v1alpha1
%doc README.md
%ruby_gemspecdir/google-cloud-network_connectivity-v1alpha1-0.4.0.gemspec
%ruby_gemslibdir/google-cloud-network_connectivity-v1alpha1-0.4.0

%files         -n gem-google-cloud-network-connectivity-v1alpha1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-network_connectivity-v1alpha1-0.4.0

%files         -n gem-google-cloud-bigtable
%ruby_gemspecdir/google-cloud-bigtable-2.6.0.gemspec
%ruby_gemslibdir/google-cloud-bigtable-2.6.0

%files         -n gem-google-cloud-bigtable-doc
%ruby_gemsdocdir/google-cloud-bigtable-2.6.0

%files         -n gem-google-cloud-bigquery-data-transfer
%doc README.md
%ruby_gemspecdir/google-cloud-bigquery-data_transfer-1.2.0.gemspec
%ruby_gemslibdir/google-cloud-bigquery-data_transfer-1.2.0

%files         -n gem-google-cloud-bigquery-data-transfer-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-bigquery-data_transfer-1.2.0

%files         -n gem-google-cloud-service-control-v1
%doc README.md
%ruby_gemspecdir/google-cloud-service_control-v1-0.3.1.gemspec
%ruby_gemslibdir/google-cloud-service_control-v1-0.3.1

%files         -n gem-google-cloud-service-control-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-service_control-v1-0.3.1

%files         -n gem-google-cloud-policy-troubleshooter
%doc README.md
%ruby_gemspecdir/google-cloud-policy_troubleshooter-1.1.0.gemspec
%ruby_gemslibdir/google-cloud-policy_troubleshooter-1.1.0

%files         -n gem-google-cloud-policy-troubleshooter-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-policy_troubleshooter-1.1.0

%files         -n gem-google-cloud-dataqna-v1alpha
%doc README.md
%ruby_gemspecdir/google-cloud-dataqna-v1alpha-0.2.0.gemspec
%ruby_gemslibdir/google-cloud-dataqna-v1alpha-0.2.0

%files         -n gem-google-cloud-dataqna-v1alpha-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-dataqna-v1alpha-0.2.0

%files         -n gem-google-analytics-data-v1alpha
%doc README.md
%ruby_gemspecdir/google-analytics-data-v1alpha-0.8.0.gemspec
%ruby_gemslibdir/google-analytics-data-v1alpha-0.8.0

%files         -n gem-google-analytics-data-v1alpha-doc
%doc README.md
%ruby_gemsdocdir/google-analytics-data-v1alpha-0.8.0

%files         -n gem-google-cloud-text-to-speech-v1beta1
%doc README.md
%ruby_gemspecdir/google-cloud-text_to_speech-v1beta1-0.6.0.gemspec
%ruby_gemslibdir/google-cloud-text_to_speech-v1beta1-0.6.0

%files         -n gem-google-cloud-text-to-speech-v1beta1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-text_to_speech-v1beta1-0.6.0

%files         -n gem-google-cloud-video-intelligence
%doc README.md
%ruby_gemspecdir/google-cloud-video_intelligence-3.1.0.gemspec
%ruby_gemslibdir/google-cloud-video_intelligence-3.1.0

%files         -n gem-google-cloud-video-intelligence-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-video_intelligence-3.1.0

%files         -n gem-google-cloud-build-v1
%doc README.md
%ruby_gemspecdir/google-cloud-build-v1-0.7.0.gemspec
%ruby_gemslibdir/google-cloud-build-v1-0.7.0

%files         -n gem-google-cloud-build-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-build-v1-0.7.0

%files         -n gem-google-cloud-asset
%doc README.md
%ruby_gemspecdir/google-cloud-asset-1.3.0.gemspec
%ruby_gemslibdir/google-cloud-asset-1.3.0

%files         -n gem-google-cloud-asset-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-asset-1.3.0

%files         -n gem-google-cloud-service-directory-v1
%doc README.md
%ruby_gemspecdir/google-cloud-service_directory-v1-0.3.0.gemspec
%ruby_gemslibdir/google-cloud-service_directory-v1-0.3.0

%files         -n gem-google-cloud-service-directory-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-service_directory-v1-0.3.0

%files         -n gem-google-cloud-app-engine-v1
%doc README.md
%ruby_gemspecdir/google-cloud-app_engine-v1-0.3.0.gemspec
%ruby_gemslibdir/google-cloud-app_engine-v1-0.3.0

%files         -n gem-google-cloud-app-engine-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-app_engine-v1-0.3.0

%files         -n gem-google-cloud-app-engine
%doc README.md
%ruby_gemspecdir/google-cloud-app_engine-1.0.0.gemspec
%ruby_gemslibdir/google-cloud-app_engine-1.0.0

%files         -n gem-google-cloud-app-engine-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-app_engine-1.0.0

%files         -n gem-google-cloud-bigtable-v2
%doc README.md
%ruby_gemspecdir/google-cloud-bigtable-v2-0.3.0.gemspec
%ruby_gemslibdir/google-cloud-bigtable-v2-0.3.0

%files         -n gem-google-cloud-bigtable-v2-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-bigtable-v2-0.3.0

%files         -n gem-grafeas
%doc README.md
%ruby_gemspecdir/grafeas-1.1.0.gemspec
%ruby_gemslibdir/grafeas-1.1.0

%files         -n grafeas-doc
%doc README.md
%ruby_gemsdocdir/grafeas-1.1.0

%files         -n gem-google-cloud-scheduler-v1
%doc README.md
%ruby_gemspecdir/google-cloud-scheduler-v1-0.4.0.gemspec
%ruby_gemslibdir/google-cloud-scheduler-v1-0.4.0

%files         -n gem-google-cloud-scheduler-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-scheduler-v1-0.4.0

%files         -n gem-google-cloud-talent
%doc README.md
%ruby_gemspecdir/google-cloud-talent-1.1.0.gemspec
%ruby_gemslibdir/google-cloud-talent-1.1.0

%files         -n gem-google-cloud-talent-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-talent-1.1.0

%files         -n gem-google-cloud-channel
%doc README.md
%ruby_gemspecdir/google-cloud-channel-1.0.1.gemspec
%ruby_gemslibdir/google-cloud-channel-1.0.1

%files         -n gem-google-cloud-channel-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-channel-1.0.1

%files         -n gem-google-cloud-dialogflow-v2
%doc README.md
%ruby_gemspecdir/google-cloud-dialogflow-v2-0.8.1.gemspec
%ruby_gemslibdir/google-cloud-dialogflow-v2-0.8.1

%files         -n gem-google-cloud-dialogflow-v2-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-dialogflow-v2-0.8.1

%files         -n gem-google-cloud-iot-v1
%doc README.md
%ruby_gemspecdir/google-cloud-iot-v1-0.3.0.gemspec
%ruby_gemslibdir/google-cloud-iot-v1-0.3.0

%files         -n gem-google-cloud-iot-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-iot-v1-0.3.0

%files         -n gem-google-cloud-retail
%doc README.md
%ruby_gemspecdir/google-cloud-retail-1.0.0.gemspec
%ruby_gemslibdir/google-cloud-retail-1.0.0

%files         -n gem-google-cloud-retail-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-retail-1.0.0

%files         -n gem-google-cloud-firestore-v1
%doc README.md
%ruby_gemspecdir/google-cloud-firestore-v1-0.4.1.gemspec
%ruby_gemslibdir/google-cloud-firestore-v1-0.4.1

%files         -n gem-google-cloud-firestore-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-firestore-v1-0.4.1

%files         -n gem-google-cloud-redis-v1
%doc README.md
%ruby_gemspecdir/google-cloud-redis-v1-0.5.0.gemspec
%ruby_gemslibdir/google-cloud-redis-v1-0.5.0

%files         -n gem-google-cloud-redis-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-redis-v1-0.5.0

%files         -n gem-google-cloud-text-to-speech-v1
%doc README.md
%ruby_gemspecdir/google-cloud-text_to_speech-v1-0.4.0.gemspec
%ruby_gemslibdir/google-cloud-text_to_speech-v1-0.4.0

%files         -n gem-google-cloud-text-to-speech-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-text_to_speech-v1-0.4.0

%files         -n gem-google-cloud-vision-v1p3beta1
%doc README.md
%ruby_gemspecdir/google-cloud-vision-v1p3beta1-0.5.0.gemspec
%ruby_gemslibdir/google-cloud-vision-v1p3beta1-0.5.0

%files         -n gem-google-cloud-vision-v1p3beta1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-vision-v1p3beta1-0.5.0

%files         -n gem-google-cloud-language-v1
%doc README.md
%ruby_gemspecdir/google-cloud-language-v1-0.4.0.gemspec
%ruby_gemslibdir/google-cloud-language-v1-0.4.0

%files         -n gem-google-cloud-language-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-language-v1-0.4.0

%files         -n gem-google-cloud-tasks-v2
%doc README.md
%ruby_gemspecdir/google-cloud-tasks-v2-0.4.0.gemspec
%ruby_gemslibdir/google-cloud-tasks-v2-0.4.0

%files         -n gem-google-cloud-tasks-v2-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-tasks-v2-0.4.0

%files         -n gem-google-cloud-video-transcoder
%doc README.md
%ruby_gemspecdir/google-cloud-video-transcoder-0.2.0.gemspec
%ruby_gemslibdir/google-cloud-video-transcoder-0.2.0

%files         -n gem-google-cloud-video-transcoder-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-video-transcoder-0.2.0

%files         -n gem-google-cloud-storage
%ruby_gemspecdir/google-cloud-storage-1.31.1.gemspec
%ruby_gemslibdir/google-cloud-storage-1.31.1

%files         -n gem-google-cloud-storage-doc
%ruby_gemsdocdir/google-cloud-storage-1.31.1

%files         -n gem-gcloud
%doc README.md
%ruby_gemspecdir/gcloud-0.24.1.gemspec
%ruby_gemslibdir/gcloud-0.24.1

%files         -n gem-gcloud-doc
%doc README.md
%ruby_gemsdocdir/gcloud-0.24.1

%files         -n gem-google-cloud-asset-v1beta1
%doc README.md
%ruby_gemspecdir/google-cloud-asset-v1beta1-0.2.5.gemspec
%ruby_gemslibdir/google-cloud-asset-v1beta1-0.2.5

%files         -n gem-google-cloud-asset-v1beta1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-asset-v1beta1-0.2.5

%files         -n gem-google-cloud-video-intelligence-v1beta2
%doc README.md
%ruby_gemspecdir/google-cloud-video_intelligence-v1beta2-0.4.0.gemspec
%ruby_gemslibdir/google-cloud-video_intelligence-v1beta2-0.4.0

%files         -n gem-google-cloud-video-intelligence-v1beta2-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-video_intelligence-v1beta2-0.4.0

%files         -n gem-google-cloud-translate
%doc README.md
%ruby_gemspecdir/google-cloud-translate-3.2.0.gemspec
%ruby_gemslibdir/google-cloud-translate-3.2.0

%files         -n gem-google-cloud-translate-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-translate-3.2.0

%files         -n gem-google-cloud-web-security-scanner-v1beta
%doc README.md
%ruby_gemspecdir/google-cloud-web_security_scanner-v1beta-0.3.0.gemspec
%ruby_gemslibdir/google-cloud-web_security_scanner-v1beta-0.3.0

%files         -n gem-google-cloud-web-security-scanner-v1beta-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-web_security_scanner-v1beta-0.3.0

%files         -n gem-google-cloud-kms-v1
%doc README.md
%ruby_gemspecdir/google-cloud-kms-v1-0.5.0.gemspec
%ruby_gemslibdir/google-cloud-kms-v1-0.5.0

%files         -n gem-google-cloud-kms-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-kms-v1-0.5.0

%files         -n gem-google-cloud-datastore
%ruby_gemspecdir/google-cloud-datastore-2.2.0.gemspec
%ruby_gemslibdir/google-cloud-datastore-2.2.0

%files         -n gem-google-cloud-datastore-doc
%ruby_gemsdocdir/google-cloud-datastore-2.2.0

%files         -n gem-google-cloud-recaptcha-enterprise-v1beta1
%doc README.md
%ruby_gemspecdir/google-cloud-recaptcha_enterprise-v1beta1-0.4.0.gemspec
%ruby_gemslibdir/google-cloud-recaptcha_enterprise-v1beta1-0.4.0

%files         -n gem-google-cloud-recaptcha-enterprise-v1beta1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-recaptcha_enterprise-v1beta1-0.4.0

%files         -n gem-google-cloud-api-gateway-v1
%doc README.md
%ruby_gemspecdir/google-cloud-api_gateway-v1-0.1.0.gemspec
%ruby_gemslibdir/google-cloud-api_gateway-v1-0.1.0

%files         -n gem-google-cloud-api-gateway-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-api_gateway-v1-0.1.0

%files         -n gem-google-cloud-bigquery
%ruby_gemspecdir/google-cloud-bigquery-1.31.0.gemspec
%ruby_gemslibdir/google-cloud-bigquery-1.31.0

%files         -n gem-google-cloud-bigquery-doc
%ruby_gemsdocdir/google-cloud-bigquery-1.31.0

%files         -n gem-google-cloud-bigtable-admin-v2
%doc README.md
%ruby_gemspecdir/google-cloud-bigtable-admin-v2-0.5.1.gemspec
%ruby_gemslibdir/google-cloud-bigtable-admin-v2-0.5.1

%files         -n gem-google-cloud-bigtable-admin-v2-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-bigtable-admin-v2-0.5.1

%files         -n gem-google-cloud-network-connectivity
%doc README.md
%ruby_gemspecdir/google-cloud-network_connectivity-0.2.0.gemspec
%ruby_gemslibdir/google-cloud-network_connectivity-0.2.0

%files         -n gem-google-cloud-network-connectivity-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-network_connectivity-0.2.0

%files         -n gem-google-cloud-media-translation-v1beta1
%doc README.md
%ruby_gemspecdir/google-cloud-media_translation-v1beta1-0.4.0.gemspec
%ruby_gemslibdir/google-cloud-media_translation-v1beta1-0.4.0

%files         -n gem-google-cloud-media-translation-v1beta1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-media_translation-v1beta1-0.4.0

%files         -n gem-google-cloud-os-config-v1
%doc README.md
%ruby_gemspecdir/google-cloud-os_config-v1-0.4.0.gemspec
%ruby_gemslibdir/google-cloud-os_config-v1-0.4.0

%files         -n gem-google-cloud-os-config-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-os_config-v1-0.4.0

%files         -n gem-google-cloud-web-risk-v1
%doc README.md
%ruby_gemspecdir/google-cloud-web_risk-v1-0.4.0.gemspec
%ruby_gemslibdir/google-cloud-web_risk-v1-0.4.0

%files         -n gem-google-cloud-web-risk-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-web_risk-v1-0.4.0

%files         -n gem-google-cloud-pubsub
%ruby_gemspecdir/google-cloud-pubsub-2.6.1.gemspec
%ruby_gemslibdir/google-cloud-pubsub-2.6.1

%files         -n gem-google-cloud-pubsub-doc
%ruby_gemsdocdir/google-cloud-pubsub-2.6.1

%files         -n gem-google-cloud-security-private-ca-v1beta1
%doc README.md
%ruby_gemspecdir/google-cloud-security-private_ca-v1beta1-0.3.0.gemspec
%ruby_gemslibdir/google-cloud-security-private_ca-v1beta1-0.3.0

%files         -n gem-google-cloud-security-private-ca-v1beta1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-security-private_ca-v1beta1-0.3.0

%files         -n gem-google-cloud-service-control
%doc README.md
%ruby_gemspecdir/google-cloud-service_control-0.2.1.gemspec
%ruby_gemslibdir/google-cloud-service_control-0.2.1

%files         -n gem-google-cloud-service-control-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-service_control-0.2.1

%files         -n gem-google-cloud-iot
%doc README.md
%ruby_gemspecdir/google-cloud-iot-1.0.0.gemspec
%ruby_gemslibdir/google-cloud-iot-1.0.0

%files         -n gem-google-cloud-iot-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-iot-1.0.0

%files         -n gem-google-cloud-service-directory-v1beta1
%doc README.md
%ruby_gemspecdir/google-cloud-service_directory-v1beta1-0.6.0.gemspec
%ruby_gemslibdir/google-cloud-service_directory-v1beta1-0.6.0

%files         -n gem-google-cloud-service-directory-v1beta1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-service_directory-v1beta1-0.6.0

%files         -n gem-google-iam-credentials-v1
%doc README.md
%ruby_gemspecdir/google-iam-credentials-v1-0.3.0.gemspec
%ruby_gemslibdir/google-iam-credentials-v1-0.3.0

%files         -n gem-google-iam-credentials-v1-doc
%doc README.md
%ruby_gemsdocdir/google-iam-credentials-v1-0.3.0

%files         -n gem-google-cloud-logging-v2
%doc README.md
%ruby_gemspecdir/google-cloud-logging-v2-0.5.0.gemspec
%ruby_gemslibdir/google-cloud-logging-v2-0.5.0

%files         -n gem-google-cloud-logging-v2-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-logging-v2-0.5.0

%files         -n gem-google-cloud-access-approval
%doc README.md
%ruby_gemspecdir/google-cloud-access_approval-1.1.0.gemspec
%ruby_gemslibdir/google-cloud-access_approval-1.1.0

%files         -n gem-google-cloud-access-approval-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-access_approval-1.1.0

%files         -n gem-google-cloud-redis-v1beta1
%doc README.md
%ruby_gemspecdir/google-cloud-redis-v1beta1-0.4.0.gemspec
%ruby_gemslibdir/google-cloud-redis-v1beta1-0.4.0

%files         -n gem-google-cloud-redis-v1beta1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-redis-v1beta1-0.4.0

%files         -n gem-google-cloud-os-login-v1beta
%doc README.md
%ruby_gemspecdir/google-cloud-os_login-v1beta-0.4.0.gemspec
%ruby_gemslibdir/google-cloud-os_login-v1beta-0.4.0

%files         -n gem-google-cloud-os-login-v1beta-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-os_login-v1beta-0.4.0

%files         -n gem-google-cloud-speech-v1p1beta1
%doc README.md
%ruby_gemspecdir/google-cloud-speech-v1p1beta1-0.9.0.gemspec
%ruby_gemslibdir/google-cloud-speech-v1p1beta1-0.9.0

%files         -n gem-google-cloud-speech-v1p1beta1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-speech-v1p1beta1-0.9.0

%files         -n gem-google-cloud-notebooks
%doc README.md
%ruby_gemspecdir/google-cloud-notebooks-1.1.0.gemspec
%ruby_gemslibdir/google-cloud-notebooks-1.1.0

%files         -n gem-google-cloud-notebooks-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-notebooks-1.1.0

%files         -n gem-google-cloud-billing
%doc README.md
%ruby_gemspecdir/google-cloud-billing-1.1.0.gemspec
%ruby_gemslibdir/google-cloud-billing-1.1.0

%files         -n gem-google-cloud-billing-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-billing-1.1.0

%files         -n gem-google-cloud-gke-hub-v1beta1
%doc README.md
%ruby_gemspecdir/google-cloud-gke_hub-v1beta1-0.1.0.gemspec
%ruby_gemslibdir/google-cloud-gke_hub-v1beta1-0.1.0

%files         -n gem-google-cloud-gke-hub-v1beta1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-gke_hub-v1beta1-0.1.0

%files         -n gem-google-cloud-document-ai
%doc README.md
%ruby_gemspecdir/google-cloud-document_ai-0.3.0.gemspec
%ruby_gemslibdir/google-cloud-document_ai-0.3.0

%files         -n gem-google-cloud-document-ai-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-document_ai-0.3.0

%files         -n gem-google-cloud-data-catalog-v1
%doc README.md
%ruby_gemspecdir/google-cloud-data_catalog-v1-0.7.1.gemspec
%ruby_gemslibdir/google-cloud-data_catalog-v1-0.7.1

%files         -n gem-google-cloud-data-catalog-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-data_catalog-v1-0.7.1

%files         -n gem-google-area120-tables
%doc README.md
%ruby_gemspecdir/google-area120-tables-0.2.0.gemspec
%ruby_gemslibdir/google-area120-tables-0.2.0

%files         -n gem-google-area120-tables-doc
%doc README.md
%ruby_gemsdocdir/google-area120-tables-0.2.0

%files         -n gem-google-cloud-trace-v1
%doc README.md
%ruby_gemspecdir/google-cloud-trace-v1-0.3.0.gemspec
%ruby_gemslibdir/google-cloud-trace-v1-0.3.0

%files         -n gem-google-cloud-trace-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-trace-v1-0.3.0

%files         -n gem-google-cloud-debugger
%ruby_gemspecdir/google-cloud-debugger-0.42.0.gemspec
%ruby_gemslibdir/google-cloud-debugger-0.42.0
%ruby_gemsextdir/google-cloud-debugger-0.42.0

%files         -n gem-google-cloud-debugger-doc
%ruby_gemsdocdir/google-cloud-debugger-0.42.0

%files         -n gem-google-cloud
%doc README.md
%ruby_gemspecdir/google-cloud-0.64.0.gemspec
%ruby_gemslibdir/google-cloud-0.64.0

%files         -n gem-google-cloud-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-0.64.0

%files         -n gem-google-cloud-recommendation-engine
%doc README.md
%ruby_gemspecdir/google-cloud-recommendation_engine-0.2.0.gemspec
%ruby_gemslibdir/google-cloud-recommendation_engine-0.2.0

%files         -n gem-google-cloud-recommendation-engine-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-recommendation_engine-0.2.0

%files         -n gem-google-cloud-container-analysis-v1
%doc README.md
%ruby_gemspecdir/google-cloud-container_analysis-v1-0.4.0.gemspec
%ruby_gemslibdir/google-cloud-container_analysis-v1-0.4.0

%files         -n gem-google-cloud-container-analysis-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-container_analysis-v1-0.4.0

%files         -n gem-google-cloud-phishing-protection-v1beta1
%doc README.md
%ruby_gemspecdir/google-cloud-phishing_protection-v1beta1-0.3.0.gemspec
%ruby_gemslibdir/google-cloud-phishing_protection-v1beta1-0.3.0

%files         -n gem-google-cloud-phishing-protection-v1beta1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-phishing_protection-v1beta1-0.3.0

%files         -n gem-google-cloud-os-config
%doc README.md
%ruby_gemspecdir/google-cloud-os_config-1.1.0.gemspec
%ruby_gemslibdir/google-cloud-os_config-1.1.0

%files         -n gem-google-cloud-os-config-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-os_config-1.1.0

%files         -n gem-google-cloud-redis
%doc README.md
%ruby_gemspecdir/google-cloud-redis-1.2.0.gemspec
%ruby_gemslibdir/google-cloud-redis-1.2.0

%files         -n gem-google-cloud-redis-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-redis-1.2.0

%files         -n gem-google-cloud-spanner
%ruby_gemspecdir/google-cloud-spanner-2.6.0.gemspec
%ruby_gemslibdir/google-cloud-spanner-2.6.0

%files         -n gem-google-cloud-spanner-doc
%ruby_gemsdocdir/google-cloud-spanner-2.6.0

%files         -n gem-google-cloud-translate-v3
%doc README.md
%ruby_gemspecdir/google-cloud-translate-v3-0.3.0.gemspec
%ruby_gemslibdir/google-cloud-translate-v3-0.3.0

%files         -n gem-google-cloud-translate-v3-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-translate-v3-0.3.0

%files         -n gem-google-cloud-os-login-v1
%doc README.md
%ruby_gemspecdir/google-cloud-os_login-v1-0.4.0.gemspec
%ruby_gemslibdir/google-cloud-os_login-v1-0.4.0

%files         -n gem-google-cloud-os-login-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-os_login-v1-0.4.0

%files         -n gem-google-cloud-metastore-v1
%doc README.md
%ruby_gemspecdir/google-cloud-metastore-v1-0.1.0.gemspec
%ruby_gemslibdir/google-cloud-metastore-v1-0.1.0

%files         -n gem-google-cloud-metastore-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-metastore-v1-0.1.0

%files         -n gem-google-cloud-dataproc
%doc README.md
%ruby_gemspecdir/google-cloud-dataproc-1.2.0.gemspec
%ruby_gemslibdir/google-cloud-dataproc-1.2.0

%files         -n gem-google-cloud-dataproc-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-dataproc-1.2.0

%files         -n gem-google-cloud-memcache
%doc README.md
%ruby_gemspecdir/google-cloud-memcache-1.1.0.gemspec
%ruby_gemslibdir/google-cloud-memcache-1.1.0

%files         -n gem-google-cloud-memcache-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-memcache-1.1.0

%files         -n gem-google-cloud-secret-manager-v1
%doc README.md
%ruby_gemspecdir/google-cloud-secret_manager-v1-0.10.0.gemspec
%ruby_gemslibdir/google-cloud-secret_manager-v1-0.10.0

%files         -n gem-google-cloud-secret-manager-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-secret_manager-v1-0.10.0

%files         -n gem-google-cloud-recaptcha-enterprise
%doc README.md
%ruby_gemspecdir/google-cloud-recaptcha_enterprise-1.2.0.gemspec
%ruby_gemslibdir/google-cloud-recaptcha_enterprise-1.2.0

%files         -n gem-google-cloud-recaptcha-enterprise-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-recaptcha_enterprise-1.2.0

%files         -n gem-stackdriver
%ruby_gemspecdir/stackdriver-0.21.1.gemspec
%ruby_gemslibdir/stackdriver-0.21.1

%files         -n stackdriver-doc
%ruby_gemsdocdir/stackdriver-0.21.1

%files         -n gem-google-cloud-bigquery-connection
%doc README.md
%ruby_gemspecdir/google-cloud-bigquery-connection-1.1.0.gemspec
%ruby_gemslibdir/google-cloud-bigquery-connection-1.1.0

%files         -n gem-google-cloud-bigquery-connection-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-bigquery-connection-1.1.0

%files         -n gem-google-cloud-dataqna
%doc README.md
%ruby_gemspecdir/google-cloud-dataqna-0.2.0.gemspec
%ruby_gemslibdir/google-cloud-dataqna-0.2.0

%files         -n gem-google-cloud-dataqna-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-dataqna-0.2.0

%files         -n gem-google-cloud-media-translation
%doc README.md
%ruby_gemspecdir/google-cloud-media_translation-0.2.0.gemspec
%ruby_gemslibdir/google-cloud-media_translation-0.2.0

%files         -n gem-google-cloud-media-translation-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-media_translation-0.2.0

%files         -n gem-google-cloud-phishing-protection
%doc README.md
%ruby_gemspecdir/google-cloud-phishing_protection-0.11.0.gemspec
%ruby_gemslibdir/google-cloud-phishing_protection-0.11.0

%files         -n gem-google-cloud-phishing-protection-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-phishing_protection-0.11.0

%files         -n gem-google-cloud-memcache-v1
%doc README.md
%ruby_gemspecdir/google-cloud-memcache-v1-0.2.0.gemspec
%ruby_gemslibdir/google-cloud-memcache-v1-0.2.0

%files         -n gem-google-cloud-memcache-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-memcache-v1-0.2.0

%files         -n gem-google-cloud-memcache-v1beta2
%doc README.md
%ruby_gemspecdir/google-cloud-memcache-v1beta2-0.2.0.gemspec
%ruby_gemslibdir/google-cloud-memcache-v1beta2-0.2.0

%files         -n gem-google-cloud-memcache-v1beta2-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-memcache-v1beta2-0.2.0

%files         -n gem-google-cloud-binary-authorization
%doc README.md
%ruby_gemspecdir/google-cloud-binary_authorization-0.2.0.gemspec
%ruby_gemslibdir/google-cloud-binary_authorization-0.2.0

%files         -n gem-google-cloud-binary-authorization-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-binary_authorization-0.2.0

%files         -n gem-stackdriver-core
%ruby_gemspecdir/stackdriver-core-1.5.0.gemspec
%ruby_gemslibdir/stackdriver-core-1.5.0

%files         -n stackdriver-core-doc
%ruby_gemsdocdir/stackdriver-core-1.5.0

%files         -n gem-google-cloud-profiler-v2
%doc README.md
%ruby_gemspecdir/google-cloud-profiler-v2-0.2.0.gemspec
%ruby_gemslibdir/google-cloud-profiler-v2-0.2.0

%files         -n gem-google-cloud-profiler-v2-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-profiler-v2-0.2.0

%files         -n gem-google-iam-v1beta
%doc README.md
%ruby_gemspecdir/google-iam-v1beta-0.3.0.gemspec
%ruby_gemslibdir/google-iam-v1beta-0.3.0

%files         -n gem-google-iam-v1beta-doc
%doc README.md
%ruby_gemsdocdir/google-iam-v1beta-0.3.0

%files         -n gem-google-cloud-automl-v1
%doc README.md
%ruby_gemspecdir/google-cloud-automl-v1-0.4.0.gemspec
%ruby_gemslibdir/google-cloud-automl-v1-0.4.0

%files         -n gem-google-cloud-automl-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-automl-v1-0.4.0

%files         -n gem-google-cloud-billing-v1
%doc README.md
%ruby_gemspecdir/google-cloud-billing-v1-0.7.0.gemspec
%ruby_gemslibdir/google-cloud-billing-v1-0.7.0

%files         -n gem-google-cloud-billing-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-billing-v1-0.7.0

%files         -n gem-google-cloud-os-login
%doc README.md
%ruby_gemspecdir/google-cloud-os_login-1.2.0.gemspec
%ruby_gemslibdir/google-cloud-os_login-1.2.0

%files         -n gem-google-cloud-os-login-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-os_login-1.2.0

%files         -n gem-google-cloud-gke-hub
%doc README.md
%ruby_gemspecdir/google-cloud-gke_hub-0.1.0.gemspec
%ruby_gemslibdir/google-cloud-gke_hub-0.1.0

%files         -n gem-google-cloud-gke-hub-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-gke_hub-0.1.0

%files         -n gem-google-cloud-language-v1beta2
%doc README.md
%ruby_gemspecdir/google-cloud-language-v1beta2-0.4.0.gemspec
%ruby_gemslibdir/google-cloud-language-v1beta2-0.4.0

%files         -n gem-google-cloud-language-v1beta2-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-language-v1beta2-0.4.0

%files         -n gem-google-cloud-scheduler
%doc README.md
%ruby_gemspecdir/google-cloud-scheduler-2.2.0.gemspec
%ruby_gemslibdir/google-cloud-scheduler-2.2.0

%files         -n gem-google-cloud-scheduler-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-scheduler-2.2.0

%files         -n gem-google-cloud-recaptcha-enterprise-v1
%doc README.md
%ruby_gemspecdir/google-cloud-recaptcha_enterprise-v1-0.4.0.gemspec
%ruby_gemslibdir/google-cloud-recaptcha_enterprise-v1-0.4.0

%files         -n gem-google-cloud-recaptcha-enterprise-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-recaptcha_enterprise-v1-0.4.0

%files         -n gem-google-cloud-errors
%doc README.md
%ruby_gemspecdir/google-cloud-errors-1.1.0.gemspec
%ruby_gemslibdir/google-cloud-errors-1.1.0

%files         -n gem-google-cloud-errors-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-errors-1.1.0

%files         -n gem-google-cloud-workflows
%doc README.md
%ruby_gemspecdir/google-cloud-workflows-1.1.0.gemspec
%ruby_gemslibdir/google-cloud-workflows-1.1.0

%files         -n gem-google-cloud-workflows-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-workflows-1.1.0

%files         -n gem-google-cloud-trace
%ruby_gemspecdir/google-cloud-trace-0.41.0.gemspec
%ruby_gemslibdir/google-cloud-trace-0.41.0

%files         -n gem-google-cloud-trace-doc
%ruby_gemsdocdir/google-cloud-trace-0.41.0

%files         -n gem-google-cloud-container-v1
%doc README.md
%ruby_gemspecdir/google-cloud-container-v1-0.5.0.gemspec
%ruby_gemslibdir/google-cloud-container-v1-0.5.0

%files         -n gem-google-cloud-container-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-container-v1-0.5.0

%files         -n gem-google-cloud-security-center
%doc README.md
%ruby_gemspecdir/google-cloud-security_center-1.2.0.gemspec
%ruby_gemslibdir/google-cloud-security_center-1.2.0

%files         -n gem-google-cloud-security-center-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-security_center-1.2.0

%files         -n gem-google-cloud-recommendation-engine-v1beta1
%doc README.md
%ruby_gemspecdir/google-cloud-recommendation_engine-v1beta1-0.3.1.gemspec
%ruby_gemslibdir/google-cloud-recommendation_engine-v1beta1-0.3.1

%files         -n gem-google-cloud-recommendation-engine-v1beta1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-recommendation_engine-v1beta1-0.3.1

%files         -n gem-google-cloud-assured-workloads
%doc README.md
%ruby_gemspecdir/google-cloud-assured_workloads-0.2.0.gemspec
%ruby_gemslibdir/google-cloud-assured_workloads-0.2.0

%files         -n gem-google-cloud-assured-workloads-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-assured_workloads-0.2.0

%files         -n gem-google-cloud-web-security-scanner
%doc README.md
%ruby_gemspecdir/google-cloud-web_security_scanner-1.0.0.gemspec
%ruby_gemslibdir/google-cloud-web_security_scanner-1.0.0

%files         -n gem-google-cloud-web-security-scanner-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-web_security_scanner-1.0.0

%files         -n gem-google-cloud-text-to-speech
%doc README.md
%ruby_gemspecdir/google-cloud-text_to_speech-1.2.0.gemspec
%ruby_gemslibdir/google-cloud-text_to_speech-1.2.0

%files         -n gem-google-cloud-text-to-speech-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-text_to_speech-1.2.0

%files         -n gem-google-cloud-org-policy
%doc README.md
%ruby_gemspecdir/google-cloud-org_policy-1.0.0.gemspec
%ruby_gemslibdir/google-cloud-org_policy-1.0.0

%files         -n gem-google-cloud-org-policy-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-org_policy-1.0.0

%files         -n gem-google-cloud-firestore-admin-v1
%doc README.md
%ruby_gemspecdir/google-cloud-firestore-admin-v1-0.3.0.gemspec
%ruby_gemslibdir/google-cloud-firestore-admin-v1-0.3.0

%files         -n gem-google-cloud-firestore-admin-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-firestore-admin-v1-0.3.0

%files         -n gem-google-cloud-dns
%ruby_gemspecdir/google-cloud-dns-0.35.0.gemspec
%ruby_gemslibdir/google-cloud-dns-0.35.0

%files         -n gem-google-cloud-dns-doc
%ruby_gemsdocdir/google-cloud-dns-0.35.0

%files         -n gem-google-cloud-video-intelligence-v1
%doc README.md
%ruby_gemspecdir/google-cloud-video_intelligence-v1-0.6.0.gemspec
%ruby_gemslibdir/google-cloud-video_intelligence-v1-0.6.0

%files         -n gem-google-cloud-video-intelligence-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-video_intelligence-v1-0.6.0

%files         -n gem-google-cloud-assured-workloads-v1beta1
%doc README.md
%ruby_gemspecdir/google-cloud-assured_workloads-v1beta1-0.6.0.gemspec
%ruby_gemslibdir/google-cloud-assured_workloads-v1beta1-0.6.0

%files         -n gem-google-cloud-assured-workloads-v1beta1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-assured_workloads-v1beta1-0.6.0

%files         -n gem-google-cloud-language
%doc README.md
%ruby_gemspecdir/google-cloud-language-1.3.0.gemspec
%ruby_gemslibdir/google-cloud-language-1.3.0

%files         -n gem-google-cloud-language-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-language-1.3.0

%files         -n gem-google-cloud-container
%doc README.md
%ruby_gemspecdir/google-cloud-container-1.2.0.gemspec
%ruby_gemslibdir/google-cloud-container-1.2.0

%files         -n gem-google-cloud-container-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-container-1.2.0

%files         -n gem-google-cloud-compute-v1
%doc README.md
%ruby_gemspecdir/google-cloud-compute-v1-0.1.0.gemspec
%ruby_gemslibdir/google-cloud-compute-v1-0.1.0

%files         -n gem-google-cloud-compute-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-compute-v1-0.1.0

%files         -n gem-google-cloud-artifact-registry-v1beta2
%doc README.md
%ruby_gemspecdir/google-cloud-artifact_registry-v1beta2-0.3.0.gemspec
%ruby_gemslibdir/google-cloud-artifact_registry-v1beta2-0.3.0

%files         -n gem-google-cloud-artifact-registry-v1beta2-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-artifact_registry-v1beta2-0.3.0

%files         -n gem-google-cloud-container-v1beta1
%doc README.md
%ruby_gemspecdir/google-cloud-container-v1beta1-0.5.1.gemspec
%ruby_gemslibdir/google-cloud-container-v1beta1-0.5.1

%files         -n gem-google-cloud-container-v1beta1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-container-v1beta1-0.5.1

%files         -n gem-google-cloud-web-risk
%doc README.md
%ruby_gemspecdir/google-cloud-web_risk-1.2.0.gemspec
%ruby_gemslibdir/google-cloud-web_risk-1.2.0

%files         -n gem-google-cloud-web-risk-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-web_risk-1.2.0

%files         -n gem-google-cloud-logging
%ruby_gemspecdir/google-cloud-logging-2.2.0.gemspec
%ruby_gemslibdir/google-cloud-logging-2.2.0

%files         -n gem-google-cloud-logging-doc
%ruby_gemsdocdir/google-cloud-logging-2.2.0

%files         -n gem-google-cloud-security-private-ca
%doc README.md
%ruby_gemspecdir/google-cloud-security-private_ca-0.2.0.gemspec
%ruby_gemslibdir/google-cloud-security-private_ca-0.2.0

%files         -n gem-google-cloud-security-private-ca-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-security-private_ca-0.2.0

%files         -n gem-google-cloud-domains
%doc README.md
%ruby_gemspecdir/google-cloud-domains-0.2.0.gemspec
%ruby_gemslibdir/google-cloud-domains-0.2.0

%files         -n gem-google-cloud-domains-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-domains-0.2.0

%files         -n gem-google-cloud-pubsub-v1
%doc README.md
%ruby_gemspecdir/google-cloud-pubsub-v1-0.4.0.gemspec
%ruby_gemslibdir/google-cloud-pubsub-v1-0.4.0

%files         -n gem-google-cloud-pubsub-v1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-pubsub-v1-0.4.0

%files         -n gem-google-cloud-dlp-v2
%doc README.md
%ruby_gemspecdir/google-cloud-dlp-v2-0.7.0.gemspec
%ruby_gemslibdir/google-cloud-dlp-v2-0.7.0

%files         -n gem-google-cloud-dlp-v2-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-dlp-v2-0.7.0

%files         -n gem-google-cloud-security-center-v1p1beta1
%doc README.md
%ruby_gemspecdir/google-cloud-security_center-v1p1beta1-0.7.0.gemspec
%ruby_gemslibdir/google-cloud-security_center-v1p1beta1-0.7.0

%files         -n gem-google-cloud-security-center-v1p1beta1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-security_center-v1p1beta1-0.7.0

%files         -n gem-google-cloud-dataproc-v1beta2
%doc README.md
%ruby_gemspecdir/google-cloud-dataproc-v1beta2-0.6.0.gemspec
%ruby_gemslibdir/google-cloud-dataproc-v1beta2-0.6.0

%files         -n gem-google-cloud-dataproc-v1beta2-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-dataproc-v1beta2-0.6.0

%files         -n gem-google-cloud-web-risk-v1beta1
%doc README.md
%ruby_gemspecdir/google-cloud-web_risk-v1beta1-0.4.0.gemspec
%ruby_gemslibdir/google-cloud-web_risk-v1beta1-0.4.0

%files         -n gem-google-cloud-web-risk-v1beta1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-web_risk-v1beta1-0.4.0

%files         -n gem-grafeas-v1
%doc README.md
%ruby_gemspecdir/grafeas-v1-0.2.0.gemspec
%ruby_gemslibdir/grafeas-v1-0.2.0

%files         -n grafeas-v1-doc
%doc README.md
%ruby_gemsdocdir/grafeas-v1-0.2.0

%files         -n gem-google-cloud-automl-v1beta1
%doc README.md
%ruby_gemspecdir/google-cloud-automl-v1beta1-0.5.0.gemspec
%ruby_gemslibdir/google-cloud-automl-v1beta1-0.5.0

%files         -n gem-google-cloud-automl-v1beta1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-automl-v1beta1-0.5.0

%files         -n gem-google-cloud-secret-manager-v1beta1
%doc README.md
%ruby_gemspecdir/google-cloud-secret_manager-v1beta1-0.8.0.gemspec
%ruby_gemslibdir/google-cloud-secret_manager-v1beta1-0.8.0

%files         -n gem-google-cloud-secret-manager-v1beta1-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-secret_manager-v1beta1-0.8.0

%files         -n gem-google-cloud-managed-identities
%doc README.md
%ruby_gemspecdir/google-cloud-managed_identities-1.0.0.gemspec
%ruby_gemslibdir/google-cloud-managed_identities-1.0.0

%files         -n gem-google-cloud-managed-identities-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-managed_identities-1.0.0

%files         -n gem-google-cloud-billing-budgets
%doc README.md
%ruby_gemspecdir/google-cloud-billing-budgets-1.1.0.gemspec
%ruby_gemslibdir/google-cloud-billing-budgets-1.1.0

%files         -n gem-google-cloud-billing-budgets-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-billing-budgets-1.1.0

%files         -n gem-google-cloud-automl
%doc README.md
%ruby_gemspecdir/google-cloud-automl-1.1.0.gemspec
%ruby_gemslibdir/google-cloud-automl-1.1.0

%files         -n gem-google-cloud-automl-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-automl-1.1.0

%files         -n gem-google-cloud-document-ai-v1beta3
%doc README.md
%ruby_gemspecdir/google-cloud-document_ai-v1beta3-0.9.0.gemspec
%ruby_gemslibdir/google-cloud-document_ai-v1beta3-0.9.0

%files         -n gem-google-cloud-document-ai-v1beta3-doc
%doc README.md
%ruby_gemsdocdir/google-cloud-document_ai-v1beta3-0.9.0

%changelog
* Mon May 31 2021 Pavel Skrylev <majioa@altlinux.org> 20210531-alt1
- + packaged gem with Ruby Policy 2.0

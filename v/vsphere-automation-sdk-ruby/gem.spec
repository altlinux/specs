Name:          vsphere-automation-sdk-ruby
Version:       20210608
Release:       alt1
Summary:       Ruby samples, language bindings, and API reference documentation for vSphere using the VMware REST API
License:       MIT
Group:         Other
Url:           https://github.com/vmware/vsphere-automation-sdk-ruby
Vcs:           https://github.com/vmware/vsphere-automation-sdk-ruby.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 2.0 gem(bundler) < 3
BuildRequires: gem(pry) >= 0.12.2 gem(pry) < 1
BuildRequires: gem(rake) >= 12.3 gem(rake) < 14
BuildRequires: gem(rspec) >= 3.7 gem(rspec) < 4
BuildRequires: gem(rubocop) >= 0.73.0 gem(rubocop) < 2
BuildRequires: gem(vcr) >= 5.0 gem(vcr) < 6
BuildRequires: gem(webmock) >= 3.6 gem(webmock) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rubocop >= 1.13.0,rubocop < 2
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
Provides:      ruby-vsphere-automation-sdk-ruby

%description
Ruby samples, language bindings, and API reference documentation for vSphere
using the VMware REST API.


%package       -n gem-vsphere-automation-appliance
Version:       0.4.7
Release:       alt1
Summary:       A Ruby SDK for the vSphere APIs (Appliance)
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(vsphere-automation-runtime) >= 0.4.6 gem(vsphere-automation-runtime) < 0.5
Requires:      gem(vsphere-automation-cis) >= 0.4.6 gem(vsphere-automation-cis) < 0.5
Provides:      gem(vsphere-automation-appliance) = 0.4.7

%description   -n gem-vsphere-automation-appliance
A Ruby SDK for the vSphere APIs (Appliance)


%package       -n gem-vsphere-automation-appliance-doc
Version:       0.4.7
Release:       alt1
Summary:       A Ruby SDK for the vSphere APIs (Appliance) documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета vsphere-automation-appliance
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(vsphere-automation-appliance) = 0.4.7

%description   -n gem-vsphere-automation-appliance-doc
A Ruby SDK for the vSphere APIs (Appliance) documentation files.

A Ruby SDK for the vSphere APIs (Appliance)

%description   -n gem-vsphere-automation-appliance-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета vsphere-automation-appliance.


%package       -n gem-vsphere-automation-appliance-devel
Version:       0.4.7
Release:       alt1
Summary:       A Ruby SDK for the vSphere APIs (Appliance) development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета vsphere-automation-appliance
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(vsphere-automation-appliance) = 0.4.7
Requires:      gem(bundler) >= 2.0 gem(bundler) < 3
Requires:      gem(pry) >= 0.12.2 gem(pry) < 1
Requires:      gem(rake) >= 12.3 gem(rake) < 14
Requires:      gem(rspec) >= 3.7 gem(rspec) < 4
Requires:      gem(rubocop) >= 0.73.0 gem(rubocop) < 2
Requires:      gem(vcr) >= 5.0 gem(vcr) < 6
Requires:      gem(webmock) >= 3.6 gem(webmock) < 4

%description   -n gem-vsphere-automation-appliance-devel
A Ruby SDK for the vSphere APIs (Appliance) development package.

A Ruby SDK for the vSphere APIs (Appliance)

%description   -n gem-vsphere-automation-appliance-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета vsphere-automation-appliance.


%package       -n gem-vsphere-automation-sdk
Version:       0.4.7
Release:       alt1
Summary:       A Ruby SDK for the vSphere APIs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(vsphere-automation-appliance) >= 0.4.6 gem(vsphere-automation-appliance) < 0.5
Requires:      gem(vsphere-automation-cis) >= 0.4.6 gem(vsphere-automation-cis) < 0.5
Requires:      gem(vsphere-automation-content) >= 0.4.6 gem(vsphere-automation-content) < 0.5
Requires:      gem(vsphere-automation-runtime) >= 0.4.6 gem(vsphere-automation-runtime) < 0.5
Requires:      gem(vsphere-automation-vapi) >= 0.4.6 gem(vsphere-automation-vapi) < 0.5
Requires:      gem(vsphere-automation-vcenter) >= 0.4.6 gem(vsphere-automation-vcenter) < 0.5
Provides:      gem(vsphere-automation-sdk) = 0.4.7

%description   -n gem-vsphere-automation-sdk
A Ruby SDK for the vSphere APIs


%package       -n gem-vsphere-automation-sdk-doc
Version:       0.4.7
Release:       alt1
Summary:       A Ruby SDK for the vSphere APIs documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета vsphere-automation-sdk
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(vsphere-automation-sdk) = 0.4.7

%description   -n gem-vsphere-automation-sdk-doc
A Ruby SDK for the vSphere APIs documentation files.

A Ruby SDK for the vSphere APIs

%description   -n gem-vsphere-automation-sdk-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета vsphere-automation-sdk.


%package       -n gem-vsphere-automation-sdk-devel
Version:       0.4.7
Release:       alt1
Summary:       A Ruby SDK for the vSphere APIs development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета vsphere-automation-sdk
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(vsphere-automation-sdk) = 0.4.7
Requires:      gem(rake) >= 12.3 gem(rake) < 14

%description   -n gem-vsphere-automation-sdk-devel
A Ruby SDK for the vSphere APIs development package.

A Ruby SDK for the vSphere APIs

%description   -n gem-vsphere-automation-sdk-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета vsphere-automation-sdk.


%package       -n gem-vsphere-automation-content
Version:       0.4.7
Release:       alt1
Summary:       A Ruby SDK for the vSphere APIs (Content)
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(vsphere-automation-runtime) >= 0.4.6 gem(vsphere-automation-runtime) < 0.5
Requires:      gem(vsphere-automation-cis) >= 0.4.6 gem(vsphere-automation-cis) < 0.5
Provides:      gem(vsphere-automation-content) = 0.4.7

%description   -n gem-vsphere-automation-content
A Ruby SDK for the vSphere APIs (Content)


%package       -n gem-vsphere-automation-content-doc
Version:       0.4.7
Release:       alt1
Summary:       A Ruby SDK for the vSphere APIs (Content) documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета vsphere-automation-content
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(vsphere-automation-content) = 0.4.7

%description   -n gem-vsphere-automation-content-doc
A Ruby SDK for the vSphere APIs (Content) documentation files.

A Ruby SDK for the vSphere APIs (Content)

%description   -n gem-vsphere-automation-content-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета vsphere-automation-content.


%package       -n gem-vsphere-automation-content-devel
Version:       0.4.7
Release:       alt1
Summary:       A Ruby SDK for the vSphere APIs (Content) development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета vsphere-automation-content
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(vsphere-automation-content) = 0.4.7
Requires:      gem(bundler) >= 2.0 gem(bundler) < 3
Requires:      gem(pry) >= 0.12.2 gem(pry) < 1
Requires:      gem(rake) >= 12.3 gem(rake) < 14
Requires:      gem(rspec) >= 3.7 gem(rspec) < 4
Requires:      gem(rubocop) >= 0.73.0 gem(rubocop) < 2
Requires:      gem(vcr) >= 5.0 gem(vcr) < 6
Requires:      gem(webmock) >= 3.6 gem(webmock) < 4

%description   -n gem-vsphere-automation-content-devel
A Ruby SDK for the vSphere APIs (Content) development package.

A Ruby SDK for the vSphere APIs (Content)

%description   -n gem-vsphere-automation-content-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета vsphere-automation-content.


%package       -n gem-vsphere-automation-cis
Version:       0.4.7
Release:       alt1
Summary:       A Ruby SDK for the vSphere REST APIs (CIS)
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(vsphere-automation-runtime) >= 0.4.6 gem(vsphere-automation-runtime) < 0.5
Provides:      gem(vsphere-automation-cis) = 0.4.7

%description   -n gem-vsphere-automation-cis
A Ruby SDK for the vSphere REST APIs (CIS)


%package       -n gem-vsphere-automation-cis-doc
Version:       0.4.7
Release:       alt1
Summary:       A Ruby SDK for the vSphere REST APIs (CIS) documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета vsphere-automation-cis
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(vsphere-automation-cis) = 0.4.7

%description   -n gem-vsphere-automation-cis-doc
A Ruby SDK for the vSphere REST APIs (CIS) documentation files.

A Ruby SDK for the vSphere REST APIs (CIS)

%description   -n gem-vsphere-automation-cis-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета vsphere-automation-cis.


%package       -n gem-vsphere-automation-cis-devel
Version:       0.4.7
Release:       alt1
Summary:       A Ruby SDK for the vSphere REST APIs (CIS) development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета vsphere-automation-cis
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(vsphere-automation-cis) = 0.4.7
Requires:      gem(bundler) >= 2.0 gem(bundler) < 3
Requires:      gem(pry) >= 0.12.2 gem(pry) < 1
Requires:      gem(rake) >= 12.3 gem(rake) < 14
Requires:      gem(rspec) >= 3.7 gem(rspec) < 4
Requires:      gem(rubocop) >= 0.73.0 gem(rubocop) < 2
Requires:      gem(vcr) >= 5.0 gem(vcr) < 6
Requires:      gem(webmock) >= 3.6 gem(webmock) < 4

%description   -n gem-vsphere-automation-cis-devel
A Ruby SDK for the vSphere REST APIs (CIS) development package.

A Ruby SDK for the vSphere REST APIs (CIS)

%description   -n gem-vsphere-automation-cis-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета vsphere-automation-cis.


%package       -n gem-vsphere-automation-vapi
Version:       0.4.7
Release:       alt1
Summary:       A Ruby SDK for the vSphere APIs (VAPI)
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(vsphere-automation-runtime) >= 0.4.6 gem(vsphere-automation-runtime) < 0.5
Requires:      gem(vsphere-automation-cis) >= 0.4.6 gem(vsphere-automation-cis) < 0.5
Provides:      gem(vsphere-automation-vapi) = 0.4.7

%description   -n gem-vsphere-automation-vapi
A Ruby SDK for the vSphere APIs (VAPI)


%package       -n gem-vsphere-automation-vapi-doc
Version:       0.4.7
Release:       alt1
Summary:       A Ruby SDK for the vSphere APIs (VAPI) documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета vsphere-automation-vapi
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(vsphere-automation-vapi) = 0.4.7

%description   -n gem-vsphere-automation-vapi-doc
A Ruby SDK for the vSphere APIs (VAPI) documentation files.

A Ruby SDK for the vSphere APIs (VAPI)

%description   -n gem-vsphere-automation-vapi-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета vsphere-automation-vapi.


%package       -n gem-vsphere-automation-vapi-devel
Version:       0.4.7
Release:       alt1
Summary:       A Ruby SDK for the vSphere APIs (VAPI) development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета vsphere-automation-vapi
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(vsphere-automation-vapi) = 0.4.7
Requires:      gem(bundler) >= 2.0 gem(bundler) < 3
Requires:      gem(pry) >= 0.12.2 gem(pry) < 1
Requires:      gem(rake) >= 12.3 gem(rake) < 14
Requires:      gem(rspec) >= 3.7 gem(rspec) < 4
Requires:      gem(rubocop) >= 0.73.0 gem(rubocop) < 2
Requires:      gem(vcr) >= 5.0 gem(vcr) < 6
Requires:      gem(webmock) >= 3.6 gem(webmock) < 4

%description   -n gem-vsphere-automation-vapi-devel
A Ruby SDK for the vSphere APIs (VAPI) development package.

A Ruby SDK for the vSphere APIs (VAPI)

%description   -n gem-vsphere-automation-vapi-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета vsphere-automation-vapi.


%package       -n gem-vsphere-automation-runtime
Version:       0.4.7
Release:       alt1
Summary:       A Ruby SDK for the vSphere APIs (Runtime)
Group:         Development/Ruby
BuildArch:     noarch

Provides:      gem(vsphere-automation-runtime) = 0.4.7

%description   -n gem-vsphere-automation-runtime
A Ruby SDK for the vSphere APIs (Runtime)


%package       -n gem-vsphere-automation-runtime-doc
Version:       0.4.7
Release:       alt1
Summary:       A Ruby SDK for the vSphere APIs (Runtime) documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета vsphere-automation-runtime
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(vsphere-automation-runtime) = 0.4.7

%description   -n gem-vsphere-automation-runtime-doc
A Ruby SDK for the vSphere APIs (Runtime) documentation files.

A Ruby SDK for the vSphere APIs (Runtime)

%description   -n gem-vsphere-automation-runtime-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета vsphere-automation-runtime.


%package       -n gem-vsphere-automation-runtime-devel
Version:       0.4.7
Release:       alt1
Summary:       A Ruby SDK for the vSphere APIs (Runtime) development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета vsphere-automation-runtime
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(vsphere-automation-runtime) = 0.4.7
Requires:      gem(bundler) >= 2.0 gem(bundler) < 3
Requires:      gem(pry) >= 0.12.2 gem(pry) < 1
Requires:      gem(rake) >= 12.3 gem(rake) < 14
Requires:      gem(rspec) >= 3.7 gem(rspec) < 4
Requires:      gem(rubocop) >= 0.73.0 gem(rubocop) < 2
Requires:      gem(vcr) >= 5.0 gem(vcr) < 6
Requires:      gem(webmock) >= 3.6 gem(webmock) < 4

%description   -n gem-vsphere-automation-runtime-devel
A Ruby SDK for the vSphere APIs (Runtime) development package.

A Ruby SDK for the vSphere APIs (Runtime)

%description   -n gem-vsphere-automation-runtime-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета vsphere-automation-runtime.


%package       -n gem-vsphere-automation-vcenter
Version:       0.4.7
Release:       alt1
Summary:       A Ruby SDK for the vSphere APIs (vCenter)
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(vsphere-automation-runtime) >= 0.4.6 gem(vsphere-automation-runtime) < 0.5
Requires:      gem(vsphere-automation-cis) >= 0.4.6 gem(vsphere-automation-cis) < 0.5
Provides:      gem(vsphere-automation-vcenter) = 0.4.7

%description   -n gem-vsphere-automation-vcenter
A Ruby SDK for the vSphere APIs (vCenter)


%package       -n gem-vsphere-automation-vcenter-doc
Version:       0.4.7
Release:       alt1
Summary:       A Ruby SDK for the vSphere APIs (vCenter) documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета vsphere-automation-vcenter
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(vsphere-automation-vcenter) = 0.4.7

%description   -n gem-vsphere-automation-vcenter-doc
A Ruby SDK for the vSphere APIs (vCenter) documentation files.

A Ruby SDK for the vSphere APIs (vCenter)

%description   -n gem-vsphere-automation-vcenter-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета vsphere-automation-vcenter.


%package       -n gem-vsphere-automation-vcenter-devel
Version:       0.4.7
Release:       alt1
Summary:       A Ruby SDK for the vSphere APIs (vCenter) development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета vsphere-automation-vcenter
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(vsphere-automation-vcenter) = 0.4.7
Requires:      gem(bundler) >= 2.0 gem(bundler) < 3
Requires:      gem(pry) >= 0.12.2 gem(pry) < 1
Requires:      gem(rake) >= 12.3 gem(rake) < 14
Requires:      gem(rspec) >= 3.7 gem(rspec) < 4
Requires:      gem(rubocop) >= 0.73.0 gem(rubocop) < 2
Requires:      gem(vcr) >= 5.0 gem(vcr) < 6
Requires:      gem(webmock) >= 3.6 gem(webmock) < 4

%description   -n gem-vsphere-automation-vcenter-devel
A Ruby SDK for the vSphere APIs (vCenter) development package.

A Ruby SDK for the vSphere APIs (vCenter)

%description   -n gem-vsphere-automation-vcenter-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета vsphere-automation-vcenter.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files

%files         -n gem-vsphere-automation-appliance
%ruby_gemspecdir/vsphere-automation-appliance-0.4.7.gemspec
%ruby_gemslibdir/vsphere-automation-appliance-0.4.7

%files         -n gem-vsphere-automation-appliance-doc
%ruby_gemsdocdir/vsphere-automation-appliance-0.4.7

%files         -n gem-vsphere-automation-appliance-devel

%files         -n gem-vsphere-automation-sdk
%ruby_gemspecdir/vsphere-automation-sdk-0.4.7.gemspec
%ruby_gemslibdir/vsphere-automation-sdk-0.4.7

%files         -n gem-vsphere-automation-sdk-doc
%ruby_gemsdocdir/vsphere-automation-sdk-0.4.7

%files         -n gem-vsphere-automation-sdk-devel

%files         -n gem-vsphere-automation-content
%ruby_gemspecdir/vsphere-automation-content-0.4.7.gemspec
%ruby_gemslibdir/vsphere-automation-content-0.4.7

%files         -n gem-vsphere-automation-content-doc
%ruby_gemsdocdir/vsphere-automation-content-0.4.7

%files         -n gem-vsphere-automation-content-devel

%files         -n gem-vsphere-automation-cis
%ruby_gemspecdir/vsphere-automation-cis-0.4.7.gemspec
%ruby_gemslibdir/vsphere-automation-cis-0.4.7

%files         -n gem-vsphere-automation-cis-doc
%ruby_gemsdocdir/vsphere-automation-cis-0.4.7

%files         -n gem-vsphere-automation-cis-devel

%files         -n gem-vsphere-automation-vapi
%ruby_gemspecdir/vsphere-automation-vapi-0.4.7.gemspec
%ruby_gemslibdir/vsphere-automation-vapi-0.4.7

%files         -n gem-vsphere-automation-vapi-doc
%ruby_gemsdocdir/vsphere-automation-vapi-0.4.7

%files         -n gem-vsphere-automation-vapi-devel

%files         -n gem-vsphere-automation-runtime
%ruby_gemspecdir/vsphere-automation-runtime-0.4.7.gemspec
%ruby_gemslibdir/vsphere-automation-runtime-0.4.7

%files         -n gem-vsphere-automation-runtime-doc
%ruby_gemsdocdir/vsphere-automation-runtime-0.4.7

%files         -n gem-vsphere-automation-runtime-devel

%files         -n gem-vsphere-automation-vcenter
%ruby_gemspecdir/vsphere-automation-vcenter-0.4.7.gemspec
%ruby_gemslibdir/vsphere-automation-vcenter-0.4.7

%files         -n gem-vsphere-automation-vcenter-doc
%ruby_gemsdocdir/vsphere-automation-vcenter-0.4.7

%files         -n gem-vsphere-automation-vcenter-devel


%changelog
* Tue Jun 08 2021 Pavel Skrylev <majioa@altlinux.org> 20210608-alt1
- + packaged gem with Ruby Policy 2.0

%define        gemname rbvmomi

Name:          gem-rbvmomi
Version:       3.0.0
Release:       alt1
Summary:       Ruby interface to the VMware vSphere API
License:       MIT or Ruby
Group:         Development/Ruby
Url:           https://github.com/vmware/rbvmomi
Vcs:           https://github.com/vmware/rbvmomi.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(pry) >= 0.13.1 gem(pry) < 1
BuildRequires: gem(rake) >= 13.0 gem(rake) < 14
BuildRequires: gem(simplecov) >= 0.17 gem(simplecov) < 1
BuildRequires: gem(yard) >= 0.9.25 gem(yard) < 0.10
BuildRequires: gem(test-unit) >= 3.3 gem(test-unit) < 4
BuildRequires: gem(builder) >= 3.2 gem(builder) < 4
BuildRequires: gem(json) >= 2.3 gem(json) < 3
BuildRequires: gem(nokogiri) >= 1.10 gem(nokogiri) < 2
BuildRequires: gem(optimist) >= 3.0 gem(optimist) < 4
BuildRequires: gem(httpclient) >= 0
BuildRequires: gem(htmlentities) >= 4.3.3 gem(htmlentities) < 4.4
BuildRequires: gem(nokogiri) >= 1.8.2 gem(nokogiri) < 1.9
BuildRequires: gem(oga) >= 0
BuildRequires: gem(logger-application) >= 0
BuildRequires: gem(libxml-ruby) >= 3.1.0 gem(libxml-ruby) < 3.2
BuildRequires: gem(ox) >= 0
BuildRequires: gem(curb) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(json) >= 2.1 gem(json) < 3
BuildRequires: gem(codeclimate-test-reporter) >= 0
BuildRequires: gem(pry-byebug) < 3.6
BuildRequires: gem(byebug) < 12
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency byebug >= 11.1.3,byebug < 12
%ruby_use_gem_dependency simplecov >= 0.17,simplecov < 1
%ruby_use_gem_dependency pry >= 0.13.1,pry < 1
%ruby_alias_names rbvmomi,rbvmomish
Requires:      gem(builder) >= 3.2 gem(builder) < 4
Requires:      gem(json) >= 2.3 gem(json) < 3
Requires:      gem(nokogiri) >= 1.10 gem(nokogiri) < 2
Requires:      gem(optimist) >= 3.0 gem(optimist) < 4
Obsoletes:     ruby-rbvmomi
Provides:      ruby-rbvmomi
Provides:      gem(rbvmomi) = 3.0.0


%description
RbVmomi is a Ruby interface to the vSphere API. Like the Perl and Java SDKs, you
can use it to manage ESX and vCenter servers. The current release supports the
vSphere 6.5 API. RbVmomi specific documentation is online and is meant to be
used alongside the official documentation.


%package       -n rbvmomish
Version:       3.0.0
Release:       alt1
Summary:       Ruby interface to the VMware vSphere API executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета rbvmomi
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rbvmomi) = 3.0.0

%description   -n rbvmomish
Ruby interface to the VMware vSphere API executable(s).

RbVmomi is a Ruby interface to the vSphere API. Like the Perl and Java SDKs, you
can use it to manage ESX and vCenter servers. The current release supports the
vSphere 6.5 API. RbVmomi specific documentation is online and is meant to be
used alongside the official documentation.

%description   -n rbvmomish -l ru_RU.UTF-8
Исполнямка для самоцвета rbvmomi.


%package       -n gem-rbvmomi-doc
Version:       3.0.0
Release:       alt1
Summary:       Ruby interface to the VMware vSphere API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rbvmomi
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rbvmomi) = 3.0.0

%description   -n gem-rbvmomi-doc
Ruby interface to the VMware vSphere API documentation files.

RbVmomi is a Ruby interface to the vSphere API. Like the Perl and Java SDKs, you
can use it to manage ESX and vCenter servers. The current release supports the
vSphere 6.5 API. RbVmomi specific documentation is online and is meant to be
used alongside the official documentation.

%description   -n gem-rbvmomi-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rbvmomi.


%package       -n gem-rbvmomi-devel
Version:       3.0.0
Release:       alt1
Summary:       Ruby interface to the VMware vSphere API development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rbvmomi
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rbvmomi) = 3.0.0
Requires:      gem(pry) >= 0.13.1 gem(pry) < 1
Requires:      gem(rake) >= 13.0 gem(rake) < 14
Requires:      gem(simplecov) >= 0.17 gem(simplecov) < 1
Requires:      gem(yard) >= 0.9.25 gem(yard) < 0.10
Requires:      gem(test-unit) >= 3.3 gem(test-unit) < 4

%description   -n gem-rbvmomi-devel
Ruby interface to the VMware vSphere API development package.

RbVmomi is a Ruby interface to the vSphere API. Like the Perl and Java SDKs, you
can use it to manage ESX and vCenter servers. The current release supports the
vSphere 6.5 API. RbVmomi specific documentation is online and is meant to be
used alongside the official documentation.

%description   -n gem-rbvmomi-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rbvmomi.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n rbvmomish
%doc README.md
%_bindir/rbvmomish

%files         -n gem-rbvmomi-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-rbvmomi-devel
%doc README.md


%changelog
* Mon Dec 05 2022 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- ^ 2.3.0 -> 3.0.0

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 2.3.0-alt1
- updated (^) 2.2.0 -> 2.3.0
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 2.2.0-alt1
- updated (^) 2.1.2 -> 2.2.0
- fixed (!) spec

* Thu Jun 06 2019 Pavel Skrylev <majioa@altlinux.org> 2.1.2-alt1
- updated (^) 1.13.0 -> 2.1.2

* Fri Mar 22 2019 Pavel Skrylev <majioa@altlinux.org> 1.13.0-alt2
- moved to (>) Ruby Policy 2.0
- removed (-) bug (closes #36334)

* Thu Aug 30 2018 Pavel Skrylev <majioa@altlinux.org> 1.13.0-alt1
- Initial build for Sisyphus

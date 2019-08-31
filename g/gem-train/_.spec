# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname train

Name:          gem-%pkgname
Version:       3.0.1
Release:       alt1
Summary:       Transport Interface to unify communication over SSH, WinRM, and friends
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/inspec/train/
%vcs           https://github.com/inspec/train.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%add_findreq_skiplist %ruby_gemslibdir/**/*
%gem_replace_version google-api-client ~> 0.23
%gem_replace_version googleauth ~> 0.6

%description
%summary.

Train lets you talk to your local or remote operating systems and APIs with
an unified interface.

It allows you to:

* execute commands via run_command
* interact with files via file
* identify the target operating system via os
* authenticate to API-based services and treat them like a platform

Train supports:

* Local execution
* SSH
* WinRM
* Docker
* Mock (for testing and debugging)
* AWS as an API
* Azure as an API
* VMware via PowerCLI


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%package       core
Summary:       Core for transport Interface to unify communication over SSH, WinRM, and friends
Group:         Development/Ruby
BuildArch:     noarch

%description   core
%summary.


%package       core-doc
Summary:       Documentation files for %gemname-core gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname-core
Group:         Development/Documentation
BuildArch:     noarch

%description   core-doc
Documentation files for %gemname-core gem.

%description   core-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname-core.


%prep
%setup

%build
%ruby_build --ignore=train-local-rot13,train-test-fixture

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir

%files         core
%doc README*
%ruby_gemspecdir//%pkgname-core-%version.gemspec
%ruby_gemslibdir/%pkgname-core-%version

%files         core-doc
%ruby_gemsdocdir/%pkgname-core-%version


%changelog
* Thu Aug 08 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.1-alt1
+ packaged gems with usage Ruby Policy 2.0

%define        _unpackaged_files_terminate_build 1
%define        gemname test-kitchen

Name:          gem-test-kitchen
Version:       3.6.0
Release:       alt1
Summary:       Test Kitchen is an integration tool for developing and testing infrastructure code and software on isolated target platforms
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://kitchen.ci/
Vcs:           https://github.com/test-kitchen/test-kitchen.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rb-readline) >= 0
BuildRequires: gem(aruba) >= 0.11
BuildRequires: gem(countloc) >= 0.4
BuildRequires: gem(cucumber) >= 2.1
BuildRequires: gem(fakefs) >= 2.0
BuildRequires: gem(maruku) >= 0.6
BuildRequires: gem(mocha) >= 1.11.2
BuildRequires: gem(berkshelf) >= 0
BuildRequires: gem(kitchen-dokken) >= 0
BuildRequires: gem(kitchen-inspec) >= 0
BuildRequires: gem(kitchen-vagrant) >= 0
BuildRequires: gem(chefstyle) >= 2.2.2
BuildRequires: gem(bcrypt_pbkdf) >= 1.0
BuildRequires: gem(chef-utils) >= 16.4.35
BuildRequires: gem(ed25519) >= 1.2
BuildRequires: gem(mixlib-install) >= 3.6
BuildRequires: gem(mixlib-shellout) >= 1.2
BuildRequires: gem(net-scp) >= 1.1
BuildRequires: gem(net-ssh) >= 2.9
BuildRequires: gem(net-ssh-gateway) >= 1.2
BuildRequires: gem(thor) >= 0.19
BuildRequires: gem(winrm) >= 2.0
BuildRequires: gem(winrm-elevated) >= 1.0
BuildRequires: gem(winrm-fs) >= 1.1
BuildRequires: gem(license-acceptance) >= 1.0.11
BuildConflicts: gem(aruba) >= 3.0
BuildConflicts: gem(countloc) >= 1
BuildConflicts: gem(cucumber) >= 8.1
BuildConflicts: gem(fakefs) >= 3
BuildConflicts: gem(maruku) >= 1
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(mocha) >= 3
BuildConflicts: gem(chefstyle) >= 3
BuildConflicts: gem(bcrypt_pbkdf) >= 2
BuildConflicts: gem(ed25519) >= 2
BuildConflicts: gem(mixlib-install) >= 4
BuildConflicts: gem(mixlib-shellout) >= 4.0
BuildConflicts: gem(net-scp) >= 5.0
BuildConflicts: gem(net-ssh) >= 8.0
BuildConflicts: gem(net-ssh-gateway) >= 3.0
BuildConflicts: gem(thor) >= 2
BuildConflicts: gem(winrm) >= 3
BuildConflicts: gem(winrm-elevated) >= 2
BuildConflicts: gem(winrm-fs) >= 2
BuildConflicts: gem(license-acceptance) >= 3.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency mocha >= 1.11.2,mocha < 2
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_dependency chefstyle >= 2.2.2,chefstyle < 3
Requires:      gem(bcrypt_pbkdf) >= 1.0
Requires:      gem(chef-utils) >= 16.4.35
Requires:      gem(ed25519) >= 1.2
Requires:      gem(mixlib-install) >= 3.6
Requires:      gem(mixlib-shellout) >= 1.2
Requires:      gem(net-scp) >= 1.1
Requires:      gem(net-ssh) >= 2.9
Requires:      gem(net-ssh-gateway) >= 1.2
Requires:      gem(thor) >= 0.19
Requires:      gem(winrm) >= 2.0
Requires:      gem(winrm-elevated) >= 1.0
Requires:      gem(winrm-fs) >= 1.1
Requires:      gem(license-acceptance) >= 1.0.11
Conflicts:     gem(bcrypt_pbkdf) >= 2
Conflicts:     gem(ed25519) >= 2
Conflicts:     gem(mixlib-install) >= 4
Conflicts:     gem(mixlib-shellout) >= 4.0
Conflicts:     gem(net-scp) >= 5.0
Conflicts:     gem(net-ssh) >= 8.0
Conflicts:     gem(net-ssh-gateway) >= 3.0
Conflicts:     gem(thor) >= 2
Conflicts:     gem(winrm) >= 3
Conflicts:     gem(winrm-elevated) >= 2
Conflicts:     gem(winrm-fs) >= 2
Conflicts:     gem(license-acceptance) >= 3.0
Provides:      gem(test-kitchen) = 3.6.0

%ruby_bindir_to %ruby_bindir

%description
Test Kitchen is an integration tool for developing and testing infrastructure
code and software on isolated target platforms.

The best way to understand what Test Kitchen does is to see it in action so
we're going to use it to help us write a simple Chef Infra cookbook. This
cookbook will be complete with tests that verify the cookbook does what it's
supposed to do. Test Kitchen comes at the process of software development with
an approach that embraces the idea that writing the tests first, watching them
fail, and then writing the code to make them pass is a great way to go. Also
known as red, green, refactor, it's a great way to write quality software.


%package       -n kitchen
Version:       3.6.0
Release:       alt1
Summary:       Test Kitchen is an integration tool for developing and testing infrastructure code and software on isolated target platforms executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета test-kitchen
Group:         Other
BuildArch:     noarch

Requires:      gem(test-kitchen) = 3.6.0

%description   -n kitchen
Test Kitchen is an integration tool for developing and testing infrastructure
code and software on isolated target platforms executable(s).

The best way to understand what Test Kitchen does is to see it in action so
we're going to use it to help us write a simple Chef Infra cookbook. This
cookbook will be complete with tests that verify the cookbook does what it's
supposed to do. Test Kitchen comes at the process of software development with
an approach that embraces the idea that writing the tests first, watching them
fail, and then writing the code to make them pass is a great way to go. Also
known as red, green, refactor, it's a great way to write quality software.

%description   -n kitchen -l ru_RU.UTF-8
Исполнямка для самоцвета test-kitchen.


%package       -n gem-test-kitchen-doc
Version:       3.6.0
Release:       alt1
Summary:       Test Kitchen is an integration tool for developing and testing infrastructure code and software on isolated target platforms documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета test-kitchen
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(test-kitchen) = 3.6.0

%description   -n gem-test-kitchen-doc
Test Kitchen is an integration tool for developing and testing infrastructure
code and software on isolated target platforms documentation files.

The best way to understand what Test Kitchen does is to see it in action so
we're going to use it to help us write a simple Chef Infra cookbook. This
cookbook will be complete with tests that verify the cookbook does what it's
supposed to do. Test Kitchen comes at the process of software development with
an approach that embraces the idea that writing the tests first, watching them
fail, and then writing the code to make them pass is a great way to go. Also
known as red, green, refactor, it's a great way to write quality software.

%description   -n gem-test-kitchen-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета test-kitchen.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc templates/driver/README.md.erb
%ruby_gemspec
%ruby_gemlibdir

%files         -n kitchen
%doc templates/driver/README.md.erb
%ruby_bindir/kitchen

%files         -n gem-test-kitchen-doc
%doc templates/driver/README.md.erb
%ruby_gemdocdir


%changelog
* Tue Dec 05 2023 Pavel Skrylev <majioa@altlinux.org> 3.6.0-alt1
- + packaged gem with Ruby Policy 2.0 without devel

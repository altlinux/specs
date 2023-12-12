%define        _unpackaged_files_terminate_build 1
%define        gemname kitchen-vagrant

Name:          gem-kitchen-vagrant
Version:       1.14.2
Release:       alt1
Summary:       Kitchen::Driver::Vagrant - A Vagrant Driver for Test Kitchen
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/test-kitchen/kitchen-vagrant/
Vcs:           https://github.com/test-kitchen/kitchen-vagrant.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.2
BuildRequires: gem(pry) >= 0
BuildRequires: gem(chefstyle) >= 2.2.2
BuildRequires: gem(test-kitchen) >= 1.4
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(chefstyle) >= 3
BuildConflicts: gem(test-kitchen) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency chefstyle >= 2.2.2,chefstyle < 3
Requires:      gem(test-kitchen) >= 1.4
Conflicts:     gem(test-kitchen) >= 4
Provides:      gem(kitchen-vagrant) = 1.14.2


%description
A Test Kitchen Driver for Vagrant.

This driver works by generating a single Vagrantfile for each instance in a
sandboxed directory. Since the Vagrantfile is written out on disk, Vagrant needs
absolutely no knowledge of Test Kitchen. So no Vagrant plugins are required.


%package       -n gem-kitchen-vagrant-doc
Version:       1.14.2
Release:       alt1
Summary:       Kitchen::Driver::Vagrant - A Vagrant Driver for Test Kitchen documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета kitchen-vagrant
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(kitchen-vagrant) = 1.14.2

%description   -n gem-kitchen-vagrant-doc
Kitchen::Driver::Vagrant - A Vagrant Driver for Test Kitchen documentation
files.

A Test Kitchen Driver for Vagrant.

This driver works by generating a single Vagrantfile for each instance in a
sandboxed directory. Since the Vagrantfile is written out on disk, Vagrant needs
absolutely no knowledge of Test Kitchen. So no Vagrant plugins are required.

%description   -n gem-kitchen-vagrant-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета kitchen-vagrant.


%package       -n gem-kitchen-vagrant-devel
Version:       1.14.2
Release:       alt1
Summary:       Kitchen::Driver::Vagrant - A Vagrant Driver for Test Kitchen development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета kitchen-vagrant
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(kitchen-vagrant) = 1.14.2
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 3.2
Requires:      gem(pry) >= 0
Requires:      gem(chefstyle) >= 2.2.2
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(chefstyle) >= 3

%description   -n gem-kitchen-vagrant-devel
Kitchen::Driver::Vagrant - A Vagrant Driver for Test Kitchen development
package.

A Test Kitchen Driver for Vagrant.

This driver works by generating a single Vagrantfile for each instance in a
sandboxed directory. Since the Vagrantfile is written out on disk, Vagrant needs
absolutely no knowledge of Test Kitchen. So no Vagrant plugins are required.

%description   -n gem-kitchen-vagrant-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета kitchen-vagrant.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-kitchen-vagrant-doc
%ruby_gemdocdir

%files         -n gem-kitchen-vagrant-devel


%changelog
* Tue Dec 05 2023 Pavel Skrylev <majioa@altlinux.org> 1.14.2-alt1
- + packaged gem with Ruby Policy 2.0

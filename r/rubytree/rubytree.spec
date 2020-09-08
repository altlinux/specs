%define        pkgname rubytree

Name:          %pkgname
Version:       1.0.1
Release:       alt1
Summary:       Simple implementation of the generic Tree data structure
Group:         Development/Ruby
License:       MIT
Url:           http://rubytree.anupamsg.me/
%vcs           https://github.com/evolve75/RubyTree.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(structured_warnings)

%description
Rubytree is a simple implementation of the generic Tree data structure.
This implementation is node-centric, where the individual nodes on the
tree are the primary objects and drive the structure.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch
Provides:      %pkgname-doc
Obsoletes:     %pkgname-doc

%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.

%description   -n gem-%pkgname-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build --join=lib:bin

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir


%changelog
* Tue Sep 08 2020 Andrey Cherepanov <cas@altlinux.org> 1.0.1-alt1
- New version.

* Thu Jul 18 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt2
- Use Ruby Policy 2.0

* Tue Oct 02 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- New version.
- Disable tests.

* Tue Dec 04 2012 Led <led@altlinux.ru> 0.5.2-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Sat Nov 28 2009 Alexey I. Froloff <raorn@altlinux.org> 0.5.2-alt1
- Built for Sisyphus


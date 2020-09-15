%define        pkgname rubytree

Name:          gem-%pkgname
Version:       1.0.1
Release:       alt1
Summary:       Simple implementation of the generic Tree data structure
Group:         Development/Ruby
License:       MIT
Url:           http://rubytree.anupamsg.me/
Vcs:           https://github.com/evolve75/RubyTree.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(structured_warnings)

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     %gemname < %EVR
Provides:      %gemname = %EVR

%description
Rubytree is a simple implementation of the generic Tree data structure.
This implementation is node-centric, where the individual nodes on the
tree are the primary objects and drive the structure.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch
Provides:      %pkgname-doc
Obsoletes:     %pkgname-doc

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

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


%changelog
* Tue Sep 08 2020 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- ^ 1.0.0 -> 1.0.1
- ! spec tags

* Thu Jul 18 2019 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt2
- > Ruby Policy 2.0

* Tue Oct 02 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.0-alt1
- New version.
- Disable tests.

* Tue Dec 04 2012 Led <led@altlinux.ru> 0.5.2-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Sat Nov 28 2009 Alexey I. Froloff <raorn@altlinux.org> 0.5.2-alt1
- Built for Sisyphus


%define        pkgname cfpropertylist
%define        gemname CFPropertyList

Name:          gem-%pkgname
Version:       3.0.2
Release:       alt1
Summary:       Read, write and manipulate both binary and XML property lists as defined by apple
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ckruse/CFPropertyList
Vcs:           https://github.com/ckruse/CFPropertyList.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(nokogiri)
BuildRequires: gem(libxml-ruby)

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
CFPropertyList implementation class to read, manipulate and write both
XML and binary property list files (plist(5)) as defined by Apple. Have
a look at CFPropertyList::List for more documentation.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build --use=CFPropertyList --alias=cfpropertylist

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
* Tue Sep 15 2020 Pavel Skrylev <majioa@altlinux.org> 3.0.2-alt1
- ^ 3.0.0 -> 3.0.2
- ! spec tags

* Tue Jul 23 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt3
- > Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt2.1
- Rebuild with new Ruby autorequirements.

* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt2
- Rebuild with tests.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus

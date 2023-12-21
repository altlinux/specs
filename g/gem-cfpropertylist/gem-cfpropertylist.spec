%define        _unpackaged_files_terminate_build 1
%define        gemname CFPropertyList

Name:          gem-cfpropertylist
Version:       3.0.6
Release:       alt1
Summary:       Read, write and manipulate both binary and XML property lists as defined by apple
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ckruse/CFPropertyList
Vcs:           https://github.com/ckruse/cfpropertylist.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(libxml-ruby) >= 0
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(nokogiri) >= 0
BuildRequires: gem(rake) >= 0.7.0
BuildRequires: gem(rexml) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names CFPropertyList,cfpropertylist
Requires:      gem(rexml) >= 0
Obsoletes:     ruby-CFPropertyList < %EVR
Provides:      ruby-CFPropertyList = %EVR
Provides:      gem(CFPropertyList) = 3.0.6


%description
CFPropertyList implementation class to read, manipulate and write both XML and
binary property list files (plist(5)) as defined by Apple. Have a look at
CFPropertyList::List for more documentation.


%package       -n gem-cfpropertylist-doc
Version:       3.0.6
Release:       alt1
Summary:       Read, write and manipulate both binary and XML property lists as defined by apple documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета CFPropertyList
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(CFPropertyList) = 3.0.6

%description   -n gem-cfpropertylist-doc
Read, write and manipulate both binary and XML property lists as defined by
apple documentation files.

CFPropertyList implementation class to read, manipulate and write both XML and
binary property list files (plist(5)) as defined by Apple. Have a look at
CFPropertyList::List for more documentation.

%description   -n gem-cfpropertylist-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета CFPropertyList.


%package       -n gem-cfpropertylist-devel
Version:       3.0.6
Release:       alt1
Summary:       Read, write and manipulate both binary and XML property lists as defined by apple development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета CFPropertyList
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(CFPropertyList) = 3.0.6
Requires:      gem(libxml-ruby) >= 0
Requires:      gem(minitest) >= 0
Requires:      gem(nokogiri) >= 0
Requires:      gem(rake) >= 0.7.0

%description   -n gem-cfpropertylist-devel
Read, write and manipulate both binary and XML property lists as defined by
apple development package.

CFPropertyList implementation class to read, manipulate and write both XML and
binary property list files (plist(5)) as defined by Apple. Have a look at
CFPropertyList::List for more documentation.

%description   -n gem-cfpropertylist-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета CFPropertyList.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-cfpropertylist-doc
%doc README.md README.rdoc
%ruby_gemdocdir

%files         -n gem-cfpropertylist-devel
%doc README.md README.rdoc


%changelog
* Wed Dec 20 2023 Pavel Skrylev <majioa@altlinux.org> 3.0.6-alt1
- ^ 3.0.2 -> 3.0.6

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

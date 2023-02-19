%define        gemname inifile

Name:          gem-inifile
Version:       3.0.0
Release:       alt1.2
Summary:       This is a native Ruby package for reading and writing INI files
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/TwP/inifile
Vcs:           https://github.com/twp/inifile.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bones) >= 3.8
BuildRequires: gem(bones-git) >= 1.3
BuildConflicts: gem(bones) >= 4
BuildConflicts: gem(bones-git) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(inifile) = 3.0.0


%description
Although made popular by Windows, INI files can be used on any system thanks to
their flexibility. They allow a program to store configuration data, which can
then be easily parsed and changed. Two notable systems that use the INI format
are Samba and Trac.

More information about INI files can be found on the Wikipedia Page.


%package       -n gem-inifile-doc
Version:       3.0.0
Release:       alt1.2
Summary:       This is a native Ruby package for reading and writing INI files documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета inifile
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(inifile) = 3.0.0

%description   -n gem-inifile-doc
This is a native Ruby package for reading and writing INI files documentation
files.

Although made popular by Windows, INI files can be used on any system thanks to
their flexibility. They allow a program to store configuration data, which can
then be easily parsed and changed. Two notable systems that use the INI format
are Samba and Trac.

More information about INI files can be found on the Wikipedia Page.

%description   -n gem-inifile-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета inifile.


%package       -n gem-inifile-devel
Version:       3.0.0
Release:       alt1.2
Summary:       This is a native Ruby package for reading and writing INI files development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета inifile
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(inifile) = 3.0.0
Requires:      gem(bones) >= 3.8
Requires:      gem(bones-git) >= 1.3
Conflicts:     gem(bones) >= 4
Conflicts:     gem(bones-git) >= 2

%description   -n gem-inifile-devel
This is a native Ruby package for reading and writing INI files development
package.

Although made popular by Windows, INI files can be used on any system thanks to
their flexibility. They allow a program to store configuration data, which can
then be easily parsed and changed. Two notable systems that use the INI format
are Samba and Trac.

More information about INI files can be found on the Wikipedia Page.

%description   -n gem-inifile-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета inifile.


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

%files         -n gem-inifile-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-inifile-devel
%doc README.md


%changelog
* Sat Jan 28 2023 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1.2
- ! closes build deps under check condition

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1.1
- ! spec

* Wed Apr 03 2019 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- Initial build for Sisyphus, packaged as a gem, using Ruby Policy 2.0

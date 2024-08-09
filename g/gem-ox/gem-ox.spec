%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname ox

Name:          gem-ox
Version:       2.14.18
Release:       alt1
Summary:       Ruby Optimized XML Parser
License:       MIT
Group:         Development/Ruby
Url:           http://www.ohler.com/ox
Vcs:           https://github.com/ohler55/ox.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake-compiler) >= 1.1.2
BuildRequires: gem(rubocop) >= 1.15.0
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake-compiler >= 1.1.2,rake-compiler < 2
Obsoletes:     ruby-ox < %EVR
Provides:      ruby-ox = %EVR
Provides:      gem(ox) = 2.14.18


%description
A fast XML parser and object serializer that uses only standard C lib. Optimized
XML (Ox), as the name implies was written to provide speed optimized XML
handling. It was designed to be an alternative to Nokogiri and other Ruby XML
parsers for generic XML parsing and as an alternative to Marshal for Object
serialization.


%if_enabled    doc
%package       -n gem-ox-doc
Version:       2.14.18
Release:       alt1
Summary:       Ruby Optimized XML Parser documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ox
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ox) = 2.14.18
Obsoletes:     ruby-ox-doc
Provides:      ruby-ox-doc

%description   -n gem-ox-doc
Ruby Optimized XML Parser documentation files.

A fast XML parser and object serializer that uses only standard C lib. Optimized
XML (Ox), as the name implies was written to provide speed optimized XML
handling. It was designed to be an alternative to Nokogiri and other Ruby XML
parsers for generic XML parsing and as an alternative to Marshal for Object
serialization.

%description   -n gem-ox-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ox.
%endif


%if_enabled    devel
%package       -n gem-ox-devel
Version:       2.14.18
Release:       alt1
Summary:       Ruby Optimized XML Parser development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ox
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ox) = 2.14.18
Requires:      gem(rake-compiler) >= 1.1.2
Requires:      gem(rubocop) >= 1.15.0
Conflicts:     gem(rake-compiler) >= 2
Conflicts:     gem(rubocop) >= 2

%description   -n gem-ox-devel
Ruby Optimized XML Parser development package.

A fast XML parser and object serializer that uses only standard C lib. Optimized
XML (Ox), as the name implies was written to provide speed optimized XML
handling. It was designed to be an alternative to Nokogiri and other Ruby XML
parsers for generic XML parsing and as an alternative to Marshal for Object
serialization.

%description   -n gem-ox-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ox.
%endif


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
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-ox-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-ox-devel
%doc README.md
%ruby_includedir/*
%endif


%changelog
* Fri Jul 26 2024 Pavel Skrylev <majioa@altlinux.org> 2.14.18-alt1
- ^ 2.14.10 -> 2.14.18

* Thu Mar 17 2022 Pavel Skrylev <majioa@altlinux.org> 2.14.10-alt1
- ^ 2.13.2 -> 2.14.10

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 2.13.2-alt1
- updated (^) 2.11.0 -> 2.13.2
- fixed (!) spec

* Wed Sep 11 2019 Pavel Skrylev <majioa@altlinux.org> 2.11.0-alt1.1
- fixed (!) spec according to changelog rules

* Tue Aug 27 2019 Pavel Skrylev <majioa@altlinux.org> 2.11.0-alt1
- updated (^) 2.10.0 -> 2.11.0
- fixed (!) spec

* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 2.10.0-alt2
- Use Ruby Policy 2.0

* Mon Sep 17 2018 Andrey Cherepanov <cas@altlinux.org> 2.10.0-alt1
- New version.

* Wed Jun 13 2018 Andrey Cherepanov <cas@altlinux.org> 2.9.3-alt1
- New version.

* Sat Jun 09 2018 Andrey Cherepanov <cas@altlinux.org> 2.9.2-alt1.1
- Rebuild for aarch64.

* Tue Apr 17 2018 Andrey Cherepanov <cas@altlinux.org> 2.9.2-alt1
- New version.

* Sun Apr 15 2018 Andrey Cherepanov <cas@altlinux.org> 2.9.1-alt1
- New version.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 2.9.0-alt1.1
- Rebuild with Ruby 2.5.1

* Wed Mar 14 2018 Andrey Cherepanov <cas@altlinux.org> 2.9.0-alt1
- New version.

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 2.8.4-alt1.1
- Rebuild with Ruby 2.5.0

* Mon Mar 05 2018 Andrey Cherepanov <cas@altlinux.org> 2.8.4-alt1
- New version.

* Thu Nov 02 2017 Andrey Cherepanov <cas@altlinux.org> 2.8.2-alt1
- New version

* Sat Oct 28 2017 Andrey Cherepanov <cas@altlinux.org> 2.8.1-alt1
- New version

* Sat Sep 23 2017 Andrey Cherepanov <cas@altlinux.org> 2.8.0-alt1
- New version

* Wed Sep 20 2017 Andrey Cherepanov <cas@altlinux.org> 2.7.0-alt1
- New version

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 2.6.0-alt1.1
- Rebuild with Ruby 2.4.1

* Fri Sep 01 2017 Andrey Cherepanov <cas@altlinux.org> 2.6.0-alt1
- Initial build for ALT Linux

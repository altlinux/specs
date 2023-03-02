%define        gemname olddoc

Name:          gem-olddoc
Version:       1.8.0
Release:       alt1.1
Summary:       old-fashioned Ruby documentation generator
License:       GPL-3.0+
Group:         Development/Ruby
Url:           https://80x24.org/olddoc/
Vcs:           https://80x24.org/olddoc.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source1:       olddoc.gemspec
Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rdoc) >= 4.2
BuildConflicts: gem(rdoc) >= 7
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rdoc) >= 4.2
Conflicts:     gem(rdoc) >= 7
Provides:      gem(olddoc) = 1.8.0


%description
olddoc contains old-fashioned document generators for those who do not wish to
impose bloated, new-fangled web cruft on their readers.

olddoc contains oldweb, an HTML generator without any images, frames, CSS, or
JavaScript. It is designed for users of text-based browsers and/or low-bandwidth
connections. oldweb focuses on text as it is the lowest common denominator for
accessibility and compatibility with people and hardware.


%package       -n olddoc
Version:       1.8.0
Release:       alt1.1
Summary:       old-fashioned Ruby documentation generator executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета olddoc
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(olddoc) = 1.8.0
Conflicts:     python-module-z4r-coveralls

%description   -n olddoc
old-fashioned Ruby documentation generator executable(s).

olddoc contains old-fashioned document generators for those who do not wish to
impose bloated, new-fangled web cruft on their readers.

olddoc contains oldweb, an HTML generator without any images, frames, CSS, or
JavaScript. It is designed for users of text-based browsers and/or low-bandwidth
connections. oldweb focuses on text as it is the lowest common denominator for
accessibility and compatibility with people and hardware.

%description   -n olddoc -l ru_RU.UTF-8
Исполнямка для самоцвета olddoc.


%package       -n gem-olddoc-doc
Version:       1.8.0
Release:       alt1.1
Summary:       old-fashioned Ruby documentation generator documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета olddoc
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(olddoc) = 1.8.0

%description   -n gem-olddoc-doc
old-fashioned Ruby documentation generator documentation files.

olddoc contains old-fashioned document generators for those who do not wish to
impose bloated, new-fangled web cruft on their readers.

olddoc contains oldweb, an HTML generator without any images, frames, CSS, or
JavaScript. It is designed for users of text-based browsers and/or low-bandwidth
connections. oldweb focuses on text as it is the lowest common denominator for
accessibility and compatibility with people and hardware.

%description   -n gem-olddoc-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета olddoc.


%package       -n gem-olddoc-devel
Version:       1.8.0
Release:       alt1.1
Summary:       old-fashioned Ruby documentation generator development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета olddoc
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(olddoc) = 1.8.0

%description   -n gem-olddoc-devel
old-fashioned Ruby documentation generator development package.

olddoc contains old-fashioned document generators for those who do not wish to
impose bloated, new-fangled web cruft on their readers.

olddoc contains oldweb, an HTML generator without any images, frames, CSS, or
JavaScript. It is designed for users of text-based browsers and/or low-bandwidth
connections. oldweb focuses on text as it is the lowest common denominator for
accessibility and compatibility with people and hardware.

%description   -n gem-olddoc-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета olddoc.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README lib/olddoc/readme.rb
%ruby_gemspec
%ruby_gemlibdir

%files         -n olddoc
%doc README lib/olddoc/readme.rb
%_bindir/olddoc

%files         -n gem-olddoc-doc
%doc README lib/olddoc/readme.rb
%ruby_gemdocdir

%files         -n gem-olddoc-devel
%doc README lib/olddoc/readme.rb


%changelog
* Thu Mar 02 2023 Pavel Skrylev <majioa@altlinux.org> 1.8.0-alt1.1
- ! spec

* Fri Mar 06 2020 Pavel Skrylev <majioa@altlinux.org> 1.8.0-alt1
- > Ruby Policy 2.0
- ^ 1.6.0 -> 1.8.0

* Mon Feb 04 2019 Pavel Skrylev <majioa@altlinux.org> 1.6.0-alt1
- Initial build for ALT.

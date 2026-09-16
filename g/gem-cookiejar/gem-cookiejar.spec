%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname cookiejar

Name:          gem-cookiejar
Version:       0.3.4
Release:       alt1
Summary:       The Ruby CookieJar is a library to help manage client-side cookies in pure Ruby
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           http://alkaline-solutions.com
Vcs:           https://github.com/dwaite/cookiejar.git
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(bundler) >= 0.9.3
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(rspec) >= 3.0
BuildRequires: gem(rspec-collection_matchers) >= 1.0
BuildRequires: gem(yard) >= 0.9.20
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(rspec-collection_matchers) >= 2
BuildConflicts: gem(yard) >= 1
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
Obsoletes:     ruby-cookiejar < %EVR
Provides:      ruby-cookiejar = %EVR
Provides:      gem(cookiejar) = 0.3.4

%description
The Ruby CookieJar is a library to help manage client-side cookies in pure Ruby.
It enables parsing and setting of cookie headers, alternating between multiple
'jars' of cookies at one time (such as having a set of cookies for each browser
or thread), and supports persistence of the cookies in a JSON string. Both
Netscape/RFC 2109 cookies and RFC 2965 cookies are supported.


%if_enabled    doc
%package       -n gem-cookiejar-doc
Version:       0.3.4
Release:       alt1
Summary:       The Ruby CookieJar is a library to help manage client-side cookies in pure Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета cookiejar
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(cookiejar) = 0.3.4

%description   -n gem-cookiejar-doc
The Ruby CookieJar is a library to help manage client-side cookies in pure Ruby
documentation files.

%description   -n gem-cookiejar-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета cookiejar.
%endif


%if_enabled    devel
%package       -n gem-cookiejar-devel
Version:       0.3.4
Release:       alt1
Summary:       The Ruby CookieJar is a library to help manage client-side cookies in pure Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета cookiejar
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(cookiejar) = 0.3.4
Requires:      gem(bundler) >= 0.9.3
Requires:      gem(rake) >= 10.0
Requires:      gem(rspec) >= 3.0
Requires:      gem(rspec-collection_matchers) >= 1.0
Requires:      gem(yard) >= 0.9.20
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(rspec-collection_matchers) >= 2
Conflicts:     gem(yard) >= 1

%description   -n gem-cookiejar-devel
The Ruby CookieJar is a library to help manage client-side cookies in pure Ruby
development package.

%description   -n gem-cookiejar-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета cookiejar.
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
%doc LICENSE README.markdown contributors.json
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-cookiejar-doc
%doc LICENSE README.markdown contributors.json
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-cookiejar-devel
%doc LICENSE README.markdown contributors.json
%endif


%changelog
* Wed Sep 16 2026 Pavel Skrylev <majioa@altlinux.org> 0.3.4-alt1
- ^ 0.3.3[1] -> 0.3.4

* Mon Apr 13 2020 Pavel Skrylev <majioa@altlinux.org> 0.3.3.1-alt1
- > Ruby Policy 2.0
- ^ 0.3.3 -> 0.3.3[1]
- ! spec tags and syntax

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.3-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Aug 21 2017 Andrey Cherepanov <cas@altlinux.org> 0.3.3-alt1
- New version

* Tue Apr 22 2014 Andrey Cherepanov <cas@altlinux.org> 0.3.2-alt1
- Initial build for ALT Linux

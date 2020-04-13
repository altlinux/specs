%define        pkgname cookiejar

Name:          gem-%pkgname
Version:       0.3.3.1
Release:       alt1
Summary:       The Ruby CookieJar is a library to help manage client-side cookies in pure Ruby
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           http://alkaline-solutions.com
Vcs:           https://github.com/dwaite/cookiejar.git
Packager:      Andrey Cherepanov <cas@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake)
BuildRequires: gem(yard)

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%pkgname < %EVR
Provides:      ruby-%pkgname = %EVR

%description
The Ruby CookieJar is a library to help manage client-side cookies in
pure Ruby. It enables parsing and setting of cookie headers, alternating
between multiple 'jars' of cookies at one time (such as having a set of
cookies for each browser or thread), and supports persistence of the
cookies in a JSON string. Both Netscape/RFC 2109 cookies and RFC 2965
cookies are supported.


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
%ruby_build --use=%gemname --version-replace=%version

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Mon Apr 13 2020 Pavel Skrylev <majioa@altlinux.org> 0.3.3.1-alt1
- > Ruby Policy 2.0
- ^ 0.3.3 -> 0.3.3.1pre
- ! spec tags and syntax

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.3.3-alt1.1
- Rebuild with new Ruby autorequirements.

* Mon Aug 21 2017 Andrey Cherepanov <cas@altlinux.org> 0.3.3-alt1
- New version

* Tue Apr 22 2014 Andrey Cherepanov <cas@altlinux.org> 0.3.2-alt1
- Initial build for ALT Linux

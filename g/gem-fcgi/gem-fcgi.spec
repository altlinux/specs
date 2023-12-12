%define        _unpackaged_files_terminate_build 1
%define        gemname fcgi

Name:          gem-fcgi
Version:       0.9.2.2
Release:       alt1
Summary:       FastCGI for ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/alphallc/ruby-fcgi-ng
Vcs:           https://github.com/alphallc/ruby-fcgi-ng.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
Patch:         ruby-3.patch
BuildRequires(pre): rpm-build-ruby
BuildRequires: libfcgi-devel

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-fcgi < %EVR
Provides:      ruby-fcgi = %EVR
Provides:      gem(fcgi) = 0.9.2.2


%description
FastCGI is a language independent, scalable, open extension to CGI that provides
high performance without the limitations of server specific APIs.

MoonWolf developed a library for FastCGI in
http://www.moonwolf.com/ruby/archive/. But now, he is MIA.


%package       -n gem-fcgi-doc
Version:       0.9.2.2
Release:       alt1
Summary:       FastCGI for ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fcgi
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fcgi) = 0.9.2.2

%description   -n gem-fcgi-doc
FastCGI for ruby documentation files.

FastCGI is a language independent, scalable, open extension to CGI that provides
high performance without the limitations of server specific APIs.

MoonWolf developed a library for FastCGI in
http://www.moonwolf.com/ruby/archive/. But now, he is MIA.

%description   -n gem-fcgi-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fcgi.


%package       -n gem-fcgi-devel
Version:       0.9.2.2
Release:       alt1
Summary:       FastCGI for ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fcgi
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fcgi) = 0.9.2.2
Requires:      libfcgi-devel

%description   -n gem-fcgi-devel
FastCGI for ruby development package.

FastCGI is a language independent, scalable, open extension to CGI that provides
high performance without the limitations of server specific APIs.

MoonWolf developed a library for FastCGI in
http://www.moonwolf.com/ruby/archive/. But now, he is MIA.

%description   -n gem-fcgi-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fcgi.


%prep
%setup
%autopatch

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc README.signals
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n gem-fcgi-doc
%doc README.rdoc README.signals
%ruby_gemdocdir

%files         -n gem-fcgi-devel
%doc README.rdoc README.signals


%changelog
* Mon Dec 04 2023 Pavel Skrylev <majioa@altlinux.org> 0.9.2.2-alt1
- ^ 0.9.2.1[1] -> 0.9.2.2

* Mon Jul 04 2022 Pavel Skrylev <majioa@altlinux.org> 0.9.2.1.1-alt1
- ^ 0.9.2.1 -> 0.9.2.1[1]

* Sun Apr 05 2020 Pavel Skrylev <majioa@altlinux.org> 0.9.2.1-alt3.1
- ! spec tags and syntax
- + devel package

* Mon Apr 15 2019 Pavel Skrylev <majioa@altlinux.org> 0.9.2.1-alt3
- > Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.2.1-alt2.5
- Rebuild with new Ruby autorequirements.

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.2.1-alt2.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 0.9.2.1-alt2.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.2.1-alt2.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.2.1-alt2.1
- Rebuild with Ruby 2.4.1

* Sat Mar 11 2017 Andrey Cherepanov <cas@altlinux.org> 0.9.2.1-alt2
- Rebuild with new %%ruby_sitearchdir location

* Thu Sep 22 2016 Andrey Cherepanov <cas@altlinux.org> 0.9.2.1-alt1
- New version 0.9.2.1

* Wed Mar 19 2014 Led <led@altlinux.ru> 0.8.8-alt1.2
- Rebuilt with ruby-2.0.0-alt1

* Wed Dec 05 2012 Led <led@altlinux.ru> 0.8.8-alt1.1
- Rebuilt with ruby-1.9.3-alt1

* Thu Jul 15 2010 Alexey I. Froloff <raorn@altlinux.org> 0.8.8-alt1
- [0.8.8]

* Fri Jun 26 2009 Alexey I. Froloff <raorn@altlinux.org> 0.8.7-alt2
- Rebuilt with Ruby 1.9

* Wed Apr 02 2008 Sir Raorn <raorn@altlinux.ru> 0.8.7-alt1
- [0.8.7]

* Tue Mar 28 2006 Kirill A. Shutemov <kas@altlinux.ru> 0.8.6-alt1
- first build

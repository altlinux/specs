%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname rack-accept

Name:          gem-rack-accept
Version:       0.4.5.5
Release:       alt0.1
Summary:       HTTP Accept* for Ruby/Rack
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/mjackson/rack-accept
Vcs:           https://github.com/mjackson/rack-accept.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rack) >= 0.4
BuildRequires: gem(rake) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rack) >= 0.4
Obsoletes:     ruby-rack-accept < %EVR
Provides:      ruby-rack-accept = %EVR
Provides:      gem(rack-accept) = 0.4.5.5

%ruby_use_gem_version rack-accept:0.4.5.5

%description
Rack::Accept is a suite of tools for Ruby/Rack applications that eases the
complexity of building and interpreting the Accept* family of HTTP request
headers.

Some features of the library are:

* Strict adherence to RFC 2616, specifically section 14
* Full support for the Accept, Accept-Charset, Accept-Encoding, and
  Accept-Language HTTP request headers
* May be used as Rack middleware or standalone
* A comprehensive test suite that covers many edge cases


%if_enabled    doc
%package       -n gem-rack-accept-doc
Version:       0.4.5.5
Release:       alt0.1
Summary:       HTTP Accept* for Ruby/Rack documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета rack-accept
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(rack-accept) = 0.4.5.5

%description   -n gem-rack-accept-doc
HTTP Accept* for Ruby/Rack documentation files.

Rack::Accept is a suite of tools for Ruby/Rack applications that eases the
complexity of building and interpreting the Accept* family of HTTP request
headers.

Some features of the library are:

* Strict adherence to RFC 2616, specifically section 14
* Full support for the Accept, Accept-Charset, Accept-Encoding, and
  Accept-Language HTTP request headers
* May be used as Rack middleware or standalone
* A comprehensive test suite that covers many edge cases

%description   -n gem-rack-accept-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета rack-accept.
%endif


%if_enabled    devel
%package       -n gem-rack-accept-devel
Version:       0.4.5.5
Release:       alt0.1
Summary:       HTTP Accept* for Ruby/Rack development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета rack-accept
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(rack-accept) = 0.4.5.5
Requires:      gem(rake) >= 0

%description   -n gem-rack-accept-devel
HTTP Accept* for Ruby/Rack development package.

Rack::Accept is a suite of tools for Ruby/Rack applications that eases the
complexity of building and interpreting the Accept* family of HTTP request
headers.

Some features of the library are:

* Strict adherence to RFC 2616, specifically section 14
* Full support for the Accept, Accept-Charset, Accept-Encoding, and
  Accept-Language HTTP request headers
* May be used as Rack middleware or standalone
* A comprehensive test suite that covers many edge cases

%description   -n gem-rack-accept-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета rack-accept.
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

%if_enabled    doc
%files         -n gem-rack-accept-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-rack-accept-devel
%doc README.md
%endif


%changelog
* Thu Apr 18 2024 Pavel Skrylev <majioa@altlinux.org> 0.4.5.5-alt0.1
- ^ 0.4.5[1] -> 0.4.5p5

* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.4.5.1-alt1
- ^ 0.4.5 -> 0.4.5[.1]
- > Ruby Policy 2.0

* Mon Feb 04 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.4.5-alt1
- Initial build for Sisyphus

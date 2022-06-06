%define        gemname url_escape

Name:          gem-url-escape
Version:       2009.06.24
Release:       alt1
Summary:       Fast url_escape library written in C
License:       Unlicense
Group:         Development/Ruby
Url:           http://github.com/bougyman/seedling
Vcs:           https://github.com/bougyman/seedling.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(url_escape) = 2009.06.24

%ruby_use_gem_version url_escape:2009.06.24

%description
Fast replacement for CGI.escape and Rack::Utils.escape


%package       -n gem-url-escape-doc
Version:       2009.06.24
Release:       alt1
Summary:       Fast url_escape library written in C documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета url_escape
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(url_escape) = 2009.06.24

%description   -n gem-url-escape-doc
Fast url_escape library written in C documentation files.

Fast replacement for CGI.escape and Rack::Utils.escape

%description   -n gem-url-escape-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета url_escape.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n gem-url-escape-doc
%doc README
%ruby_gemdocdir


%changelog
* Mon May 16 2022 Pavel Skrylev <majioa@altlinux.org> 2009.06.24-alt1
- + packaged gem with Ruby Policy 2.0

%define        gemname tidy-ext

Name:          gem-tidy-ext
Version:       0.1.14
Release:       alt1
Summary:       W3C HTML Tidy library implemented as a Ruby native extension
License:       Unlicense
Group:         Development/Ruby
Url:           https://bitbucket.org/carldouglas/tidy
Vcs:           https://bitbucket.org/carldouglas/tidy.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(tidy-ext) = 0.1.14


%description
Tidy up web pages.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir


%changelog
* Tue May 17 2022 Pavel Skrylev <majioa@altlinux.org> 0.1.14-alt1
- + packaged gem with Ruby Policy 2.0

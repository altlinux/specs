# vim: set ft=spec: -*- rpm-spec -*-
%define        pkgname sassc-rails

Name:          gem-%pkgname
Version:       2.1.2.1
Release:       alt1
Summary:       Integrate SassC-Ruby with Rails
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/sass/sassc-rails
Vcs:           https://github.com/sass/sassc-rails.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*

%description
%summary.

We all love working with Sass, but compilation can take quite a long time for
larger codebases. This gem integrates the C implementation of Sass, LibSass,
into the asset pipeline.

In one larger project, this made compilation 4x faster than sass-rails


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
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Tue Dec 08 2020 Pavel Skrylev <majioa@altlinux.org> 2.1.2.1-alt1
- ^ 2.1.2 -> 2.1.2[1]

* Wed Jun 10 2020 Pavel Skrylev <majioa@altlinux.org> 2.1.2-alt1
- + packaged gem with usage Ruby Policy 2.0

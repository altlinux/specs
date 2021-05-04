%define        pkgname execjs

Name:          gem-%pkgname
Version:       2.7.0.1
Release:       alt0.1
Summary:       Run JavaScript code from Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rails/execjs
Vcs:           https://github.com/rails/execjs.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
ExecJS lets you run JavaScript code from Ruby. It automatically picks the best
runtime available to evaluate your JavaScript program, then returns the result
to you as a Ruby object.

ExecJS supports these runtimes:

* therubyracer - Google V8 embedded within Ruby
* therubyrhino - Mozilla Rhino embedded within JRuby
* Duktape.rb - Duktape JavaScript interpret
* Node.js
* Apple JavaScriptCore - Included with Mac OS
* Microsoft Windows Script Host (JScript)
* Google V8
* mini_racer - Google V8 embedded within Ruby


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
* Tue Dec 15 2020 Pavel Skrylev <majioa@altlinux.org> 2.7.0.1-alt0.1
- > Ruby Policy 2.0
- ^ 2.7.0 -> 2.7.0[1]
- * renamed

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.7.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue Jun 05 2018 Andrey Cherepanov <cas@altlinux.org> 2.7.0-alt1
- Initial build for Sisyphus

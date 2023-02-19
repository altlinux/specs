%define        gemname execjs

Name:          gem-execjs
Version:       2.8.1
Release:       alt1
Summary:       Run JavaScript code from Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rails/execjs
Vcs:           https://github.com/rails/execjs.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(duktape) >= 0
BuildRequires: gem(mini_racer) >= 0
BuildRequires: gem(minitest) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-execjs < %EVR
Provides:      ruby-execjs = %EVR
Provides:      gem(execjs) = 2.8.1


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


%package       -n gem-execjs-doc
Version:       2.8.1
Release:       alt1
Summary:       Run JavaScript code from Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета execjs
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(execjs) = 2.8.1

%description   -n gem-execjs-doc
Run JavaScript code from Ruby documentation files.

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

%description   -n gem-execjs-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета execjs.


%package       -n gem-execjs-devel
Version:       2.8.1
Release:       alt1
Summary:       Run JavaScript code from Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета execjs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(execjs) = 2.8.1
Requires:      gem(rake) >= 0
Requires:      gem(duktape) >= 0
Requires:      gem(mini_racer) >= 0
Requires:      gem(therubyrhino) >= 1.73.3
Requires:      gem(minitest) >= 0

%description   -n gem-execjs-devel
Run JavaScript code from Ruby development package.

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

%description   -n gem-execjs-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета execjs.


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

%files         -n gem-execjs-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-execjs-devel
%doc README.md


%changelog
* Mon Jan 30 2023 Pavel Skrylev <majioa@altlinux.org> 2.8.1-alt1
- ^ 2.7.0.1 -> 2.8.1

* Tue Dec 15 2020 Pavel Skrylev <majioa@altlinux.org> 2.7.0.1-alt0.1
- > Ruby Policy 2.0
- ^ 2.7.0 -> 2.7.0[1]
- * renamed

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 2.7.0-alt1.1
- Rebuild with new Ruby autorequirements.

* Tue Jun 05 2018 Andrey Cherepanov <cas@altlinux.org> 2.7.0-alt1
- Initial build for Sisyphus

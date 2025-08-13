%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname execjs

Name:          gem-execjs
Version:       2.10.0
Release:       alt1
Summary:       Run JavaScript code from Ruby
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/rails/execjs
Vcs:           https://github.com/rails/execjs.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(rake) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.5.0
Obsoletes:     ruby-execjs < %EVR
Provides:      ruby-execjs = %EVR
Provides:      gem(execjs) = 2.10.0

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


%if_enabled    doc
%package       -n gem-execjs-doc
Version:       2.10.0
Release:       alt1
Summary:       Run JavaScript code from Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета execjs
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(execjs) = 2.10.0

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
%endif


%if_enabled    devel
%package       -n gem-execjs-devel
Version:       2.10.0
Release:       alt1
Summary:       Run JavaScript code from Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета execjs
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(execjs) = 2.10.0
Requires:      gem(rake) >= 0
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
%doc MIT-LICENSE README.md CONTRIBUTING.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-execjs-doc
%doc MIT-LICENSE README.md CONTRIBUTING.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-execjs-devel
%doc MIT-LICENSE README.md CONTRIBUTING.md
%endif


%changelog
* Wed Aug 13 2025 Pavel Skrylev <majioa@altlinux.org> 2.10.0-alt1
- ^ 2.8.1 -> 2.10.0

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

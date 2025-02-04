%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname erubi

Name:          gem-erubi
Version:       1.13.1
Release:       alt1
Summary:       Small ERB Implementation
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jeremyevans/erubi
Vcs:           https://github.com/jeremyevans/erubi.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(minitest-global_expectations) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-erubi < %EVR
Provides:      ruby-erubi = %EVR
Provides:      erubi = %EVR
Provides:      gem(erubi) = 1.13.1

%description
Erubi is a ERB template engine for ruby. It is a simplified fork of Erubis,
using the same basic algorithm, with the following differences:

* Handles postfix conditionals when using escaping
* Supports frozen_string_literal: true in templates via :freeze option
* Works with ruby's -enable-frozen-string-literal option
* Automatically freezes strings for template text when ruby optimizes it (on
  ruby 2.1+)
* Escapes ' (apostrophe) when escaping for better XSS protection
* Has 6x faster escaping on ruby 2.3+ by using cgi/escape
* Has 86% smaller memory footprint
* Does no monkey patching (Erubis adds a method to Kernel)
* Uses an immutable design (all options passed to the constructor, which returns
  a frozen object)
* Has simpler internals (1 file, <150 lines of code)
* Is not dead (Erubis hasn't been updated since 2011)
* It is not designed with Erubis API compatibility in mind, though most Erubis
  ERB syntax works, with the following exceptions:
* No support for debug output


%if_enabled    doc
%package       -n gem-erubi-doc
Version:       1.13.1
Release:       alt1
Summary:       Small ERB Implementation documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета erubi
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(erubi) = 1.13.1

%description   -n gem-erubi-doc
Small ERB Implementation documentation files.

Erubi is a ERB template engine for ruby. It is a simplified fork of Erubis,
using the same basic algorithm, with the following differences:

* Handles postfix conditionals when using escaping
* Supports frozen_string_literal: true in templates via :freeze option
* Works with ruby's -enable-frozen-string-literal option
* Automatically freezes strings for template text when ruby optimizes it (on
ruby 2.1+)
* Escapes ' (apostrophe) when escaping for better XSS protection
* Has 6x faster escaping on ruby 2.3+ by using cgi/escape
* Has 86% smaller memory footprint
* Does no monkey patching (Erubis adds a method to Kernel)
* Uses an immutable design (all options passed to the constructor, which returns
a frozen object)
* Has simpler internals (1 file, <150 lines of code)
* Is not dead (Erubis hasn't been updated since 2011)
* It is not designed with Erubis API compatibility in mind, though most Erubis
ERB syntax works, with the following exceptions:
* No support for debug output

%description   -n gem-erubi-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета erubi.
%endif


%if_enabled    devel
%package       -n gem-erubi-devel
Version:       1.13.1
Release:       alt1
Summary:       Small ERB Implementation development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета erubi
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(erubi) = 1.13.1
Requires:      gem(minitest) >= 0
Requires:      gem(minitest-global_expectations) >= 0

%description   -n gem-erubi-devel
Small ERB Implementation development package.

Erubi is a ERB template engine for ruby. It is a simplified fork of Erubis,
using the same basic algorithm, with the following differences:

* Handles postfix conditionals when using escaping
* Supports frozen_string_literal: true in templates via :freeze option
* Works with ruby's -enable-frozen-string-literal option
* Automatically freezes strings for template text when ruby optimizes it (on
ruby 2.1+)
* Escapes ' (apostrophe) when escaping for better XSS protection
* Has 6x faster escaping on ruby 2.3+ by using cgi/escape
* Has 86% smaller memory footprint
* Does no monkey patching (Erubis adds a method to Kernel)
* Uses an immutable design (all options passed to the constructor, which returns
a frozen object)
* Has simpler internals (1 file, <150 lines of code)
* Is not dead (Erubis hasn't been updated since 2011)
* It is not designed with Erubis API compatibility in mind, though most Erubis
ERB syntax works, with the following exceptions:
* No support for debug output

%description   -n gem-erubi-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета erubi.
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
%doc CHANGELOG MIT-LICENSE README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-erubi-doc
%doc CHANGELOG MIT-LICENSE README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-erubi-devel
%doc CHANGELOG MIT-LICENSE README.rdoc
%endif


%changelog
* Fri Jan 10 2025 Pavel Skrylev <majioa@altlinux.org> 1.13.1-alt1
- ^ 1.10.0 -> 1.13.1

* Wed Aug 25 2021 Pavel Skrylev <majioa@altlinux.org> 1.10.0-alt1
- ^ 1.8.0 -> 1.10.0

* Wed Jul 10 2019 Pavel Skrylev <majioa@altlinux.org> 1.8.0-alt1
- Bump to 1.8.0
- Use Ruby Policy 2.0

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1.7.1-alt1.1
- Rebuild with new Ruby autorequirements.

* Thu Jun 14 2018 Andrey Cherepanov <cas@altlinux.org> 1.7.1-alt1
- Initial build for Sisyphus

%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname prism

Name:          gem-prism
Version:       1.9.0
Release:       alt1
Summary:       Prism Ruby parser
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ruby/prism
Vcs:           https://github.com/ruby/prism.git
Packager:      Baltix Maintaining Team <baltix@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake libruby-devel
%if_enabled check
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(onigmo) >= 0
BuildRequires: gem(parser) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(ruby_parser) >= 0
BuildRequires: gem(test-unit) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      ruby >= 2.7.0
Requires:      gem(parser) >= 0
Requires:      gem(ruby_parser) >= 0
Provides:      gem(prism) = 1.9.0

%ruby_on_build_rake_tasks templates

%description
This is a parser for the Ruby programming language. It is designed to be
portable, error tolerant, and maintainable. It is written in C99 and has no
dependencies.

The repository contains the infrastructure for both a shared library (libprism)
and a native CRuby extension. The shared library has no bindings to CRuby
itself, and so can be used by other projects. The native CRuby extension links
against ruby.h, and so is suitable in the context of CRuby.


%if_enabled    doc
%package       -n gem-prism-doc
Version:       1.9.0
Release:       alt1
Summary:       Prism Ruby parser documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета prism
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(prism) = 1.9.0

%description   -n gem-prism-doc
Prism Ruby parser documentation files.

This is a parser for the Ruby programming language. It is designed to be
portable, error tolerant, and maintainable. It is written in C99 and has no
dependencies.

The repository contains the infrastructure for both a shared library (libprism)
and a native CRuby extension. The shared library has no bindings to CRuby
itself, and so can be used by other projects. The native CRuby extension links
against ruby.h, and so is suitable in the context of CRuby.

%description   -n gem-prism-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета prism.
%endif


%if_enabled    devel
%package       -n gem-prism-devel
Version:       1.9.0
Release:       alt1
Summary:       Prism Ruby parser development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета prism
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(prism) = 1.9.0

%description   -n gem-prism-devel
Prism Ruby parser development package.

This is a parser for the Ruby programming language. It is designed to be
portable, error tolerant, and maintainable. It is written in C99 and has no
dependencies.

The repository contains the infrastructure for both a shared library (libprism)
and a native CRuby extension. The shared library has no bindings to CRuby
itself, and so can be used by other projects. The native CRuby extension links
against ruby.h, and so is suitable in the context of CRuby.

%description   -n gem-prism-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета prism.
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
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.md README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-prism-doc
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.md README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-prism-devel
%doc CHANGELOG.md CODE_OF_CONDUCT.md CONTRIBUTING.md LICENSE.md README.md
%ruby_includedir/*
%endif


%changelog
* Mon Jun 22 2026 Pavel Skrylev <majioa@altlinux.org> 1.9.0-alt1
- ^ 1.4.0 -> 1.9.0

* Thu Aug 14 2025 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt1
- ^ 1.2.0 -> 1.4.0

* Wed Dec 11 2024 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1
- ^ 0.25.0 -> 1.2.0

* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 0.25.0-alt1
- + packaged gem with Ruby Policy 2.0

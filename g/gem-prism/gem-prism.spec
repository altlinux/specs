%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname prism

Name:          gem-prism
Version:       0.25.0
Release:       alt1
Summary:       Prism Ruby parser
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ruby/prism
Vcs:           https://github.com/ruby/prism.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(test-unit) >= 0
BuildRequires: gem(ffi) >= 0
BuildRequires: gem(parser) >= 0
BuildRequires: gem(ruby_parser) >= 0
BuildRequires: gem(benchmark-ips) >= 0
BuildRequires: gem(ruby_memcheck) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(prism) = 0.25.0


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
Version:       0.25.0
Release:       alt1
Summary:       Prism Ruby parser documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета prism
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(prism) = 0.25.0

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
Version:       0.25.0
Release:       alt1
Summary:       Prism Ruby parser development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета prism
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(prism) = 0.25.0
Requires:      gem(rake) >= 0
Requires:      gem(rake-compiler) >= 0
Requires:      gem(test-unit) >= 0
Requires:      gem(ffi) >= 0
Requires:      gem(parser) >= 0
Requires:      gem(ruby_parser) >= 0
Requires:      gem(benchmark-ips) >= 0
Requires:      gem(ruby_memcheck) >= 0

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
%doc README.md
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-prism-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-prism-devel
%doc README.md
%ruby_includedir/*
%endif


%changelog
* Mon Apr 15 2024 Pavel Skrylev <majioa@altlinux.org> 0.25.0-alt1
- + packaged gem with Ruby Policy 2.0

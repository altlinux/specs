%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%define        gemname lefthook

Name:          gem-lefthook
Version:       2.1.9
Release:       alt1
Summary:       A single dependency-free binary to manage all your git hooks that works with any language in any environment, and in all common team workflows
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/evilmartians/lefthook
Vcs:           https://github.com/evilmartians/lefthook.git
BuildArch:     noarch

Source:        %name-%version.tar
Autoprov:      yes,noruby
Autoreq:       yes,noruby
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(lefthook) = 2.1.9

%description
A single dependency-free binary to manage all your git hooks that works with any
language in any environment, and in all common team workflows.


%package       -n lefthook
Version:       2.1.9
Release:       alt1
Summary:       A single dependency-free binary to manage all your git hooks that works with any language in any environment, and in all common team workflows executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета lefthook
Group:         Other
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(lefthook) = 2.1.9

%description   -n lefthook
A single dependency-free binary to manage all your git hooks that works with any
language in any environment, and in all common team workflows executable(s).

%description   -n lefthook -l ru_RU.UTF-8
Исполнямка для самоцвета lefthook.


%if_enabled    doc
%package       -n gem-lefthook-doc
Version:       2.1.9
Release:       alt1
Summary:       A single dependency-free binary to manage all your git hooks that works with any language in any environment, and in all common team workflows documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета lefthook
Group:         Development/Documentation
BuildArch:     noarch

Autoprov:      yes,noruby
Autoreq:       yes,noruby
Requires:      gem(lefthook) = 2.1.9

%description   -n gem-lefthook-doc
A single dependency-free binary to manage all your git hooks that works with any
language in any environment, and in all common team workflows documentation
files.

%description   -n gem-lefthook-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета lefthook.
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

%files         -n lefthook
%doc README.md
%_bindir/lefthook

%if_enabled    doc
%files         -n gem-lefthook-doc
%doc README.md
%ruby_gemdocdir
%endif


%changelog
* Fri Jul 03 2026 Alexander Burmatov <thatman@altlinux.org> 2.1.9-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies

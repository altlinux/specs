%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname warning

Name:          gem-warning
Version:       1.3.0
Release:       alt1
Summary:       Add custom processing for warnings
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/jeremyevans/ruby-warning
Vcs:           https://github.com/jeremyevans/ruby-warning.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(minitest-global_expectations) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(warning) = 1.3.0


%description
ruby-warning adds custom processing for warnings, including the ability to
ignore specific warning messages, ignore warnings in specific files/directories,
include backtraces with warnings, treat warnings as errors, deduplicate
warnings, and add custom handling for all warnings in specific
files/directories.


%if_enabled    doc
%package       -n gem-warning-doc
Version:       1.3.0
Release:       alt1
Summary:       Add custom processing for warnings documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета warning
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(warning) = 1.3.0

%description   -n gem-warning-doc
Add custom processing for warnings documentation files.

ruby-warning adds custom processing for warnings, including the ability to
ignore specific warning messages, ignore warnings in specific files/directories,
include backtraces with warnings, treat warnings as errors, deduplicate
warnings, and add custom handling for all warnings in specific
files/directories.
%description   -n gem-warning-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета warning.
%endif


%if_enabled    devel
%package       -n gem-warning-devel
Version:       1.3.0
Release:       alt1
Summary:       Add custom processing for warnings development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета warning
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(warning) = 1.3.0
Requires:      gem(minitest-global_expectations) >= 0

%description   -n gem-warning-devel
Add custom processing for warnings development package.

ruby-warning adds custom processing for warnings, including the ability to
ignore specific warning messages, ignore warnings in specific files/directories,
include backtraces with warnings, treat warnings as errors, deduplicate
warnings, and add custom handling for all warnings in specific
files/directories.
%description   -n gem-warning-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета warning.
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
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-warning-doc
%doc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-warning-devel
%doc README.rdoc
%endif


%changelog
* Mon Mar 25 2024 Pavel Skrylev <majioa@altlinux.org> 1.3.0-alt1
- + packaged gem with Ruby Policy 2.0

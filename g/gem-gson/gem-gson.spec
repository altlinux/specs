%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname gson

Name:          gem-gson
Version:       0.6.1
Release:       alt1
Summary:       Ruby wrapper for GSON
License:       Unlicense
Group:         Development/Ruby
Url:           https://github.com/avsej/gson.rb
Vcs:           https://github.com/avsej/gson.rb.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(rake-compiler) >= 0.7.5
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(gson) = 0.6.1


%description
Ruby wrapper for GSON. https://code.google.com/p/google-gson/


%if_enabled    doc
%package       -n gem-gson-doc
Version:       0.6.1
Release:       alt1
Summary:       Ruby wrapper for GSON documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета gson
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(gson) = 0.6.1

%description   -n gem-gson-doc
Ruby wrapper for GSON documentation files.

Ruby wrapper for GSON. https://code.google.com/p/google-gson/

%description   -n gem-gson-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета gson.
%endif


%if_enabled    devel
%package       -n gem-gson-devel
Version:       0.6.1
Release:       alt1
Summary:       Ruby wrapper for GSON development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета gson
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(gson) = 0.6.1
Requires:      gem(rake-compiler) >= 0.7.5

%description   -n gem-gson-devel
Ruby wrapper for GSON development package.

Ruby wrapper for GSON. https://code.google.com/p/google-gson/

%description   -n gem-gson-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета gson.
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
%doc README.md benchmark/README.markdown
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-gson-doc
%doc README.md benchmark/README.markdown
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-gson-devel
%doc README.md benchmark/README.markdown
%endif


%changelog
* Tue Mar 26 2024 Pavel Skrylev <majioa@altlinux.org> 0.6.1-alt1
- + packaged gem with Ruby Policy 2.0

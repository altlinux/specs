%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname newt

Name:          gem-newt
Version:       1.1.0
Release:       alt1.1
Summary:       Ruby bindings for newt TUI library
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/theforeman/ruby-newt
Vcs:           https://github.com/theforeman/ruby-newt.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby rake setup-rb libruby-devel
BuildRequires: pkgconfig(libnewt)
BuildRequires: pkgconfig(slang)
%if_enabled check
BuildRequires: gem(minitest) >= 0
BuildRequires: gem(rake-compiler) >= 1.1.0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake-compiler >= 1.1.0
Provides:      gem(newt) = 1.1.0

%description
Ruby bindings for the newt text mode windowing library. Used by the text user
interface of Foreman Discovery Image.


%if_enabled    doc
%package       -n gem-newt-doc
Version:       1.1.0
Release:       alt1.1
Summary:       Ruby bindings for newt TUI library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета newt
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(newt) = 1.1.0

%description   -n gem-newt-doc
Ruby bindings for newt TUI library documentation files.

Ruby bindings for the newt text mode windowing library. Used by the text user
interface of Foreman Discovery Image.

%description   -n gem-newt-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета newt.
%endif


%if_enabled    devel
%package       -n gem-newt-devel
Version:       1.1.0
Release:       alt1.1
Summary:       Ruby bindings for newt TUI library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета newt
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(newt) = 1.1.0
Requires:      gem(minitest) >= 0
Requires:      gem(rake-compiler) >= 1.1.0
Requires:      libruby-devel
Requires:      pkgconfig(libnewt)
Requires:      pkgconfig(ruby)
Requires:      pkgconfig(slang)

%description   -n gem-newt-devel
Ruby bindings for newt TUI library development package.

Ruby bindings for the newt text mode windowing library. Used by the text user
interface of Foreman Discovery Image.

%description   -n gem-newt-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета newt.
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
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-newt-doc
%doc README.rdoc
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-newt-devel
%doc README.rdoc
%endif


%changelog
* Wed Nov 11 2026 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1.1
- * run the upstream test task against the built extension
- * generate the spec with Baltix and build from the tagged source tree
- ! list example files without Git and declare Ruby headers

* Wed Nov 04 2026 Pavel Vasenkov <pav@altlinux.org> 1.1.0-alt1
- Initial build for ALT Linux Sisyphus (dependency of foreman-discovery-image).
- gemspec: do not call git to list examples.

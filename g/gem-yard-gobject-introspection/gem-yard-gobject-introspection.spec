%define        _unpackaged_files_terminate_build 1
%define        gemname yard-gobject-introspection

Name:          gem-yard-gobject-introspection
Version:       0.0.1
Release:       alt0.1
Summary:       Generate documentattion for gobject-introspection libraries
License:       GPL-2.0
Group:         Development/Ruby
Url:           https://github.com/ruby-gnome2/yard-gobject-introspection
Vcs:           https://github.com/ruby-gnome2/yard-gobject-introspection.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rexml) >= 0
BuildRequires: gem(yard) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(rexml) >= 0
Requires:      gem(yard) >= 0
Provides:      gem(yard-gobject-introspection) = 0.0.1

%ruby_use_gem_version yard-gobject-introspection:0.0.1

%description
Generate documentattion for gobject-introspection libraries.


%package       -n gem-yard-gobject-introspection-doc
Version:       0.0.1
Release:       alt0.1
Summary:       Generate documentattion for gobject-introspection libraries documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета yard-gobject-introspection
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(yard-gobject-introspection) = 0.0.1

%description   -n gem-yard-gobject-introspection-doc
Generate documentattion for gobject-introspection libraries documentation files.

%description   -n gem-yard-gobject-introspection-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета yard-gobject-introspection.


%package       -n gem-yard-gobject-introspection-devel
Version:       0.0.1
Release:       alt0.1
Summary:       Generate documentattion for gobject-introspection libraries development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета yard-gobject-introspection
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(yard-gobject-introspection) = 0.0.1

%description   -n gem-yard-gobject-introspection-devel
Generate documentattion for gobject-introspection libraries development package.

%description   -n gem-yard-gobject-introspection-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета yard-gobject-introspection.


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

%files         -n gem-yard-gobject-introspection-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-yard-gobject-introspection-devel
%doc README.md


%changelog
* Sat Jun 24 2023 Pavel Skrylev <majioa@altlinux.org> 0.0.1-alt0.1
- + packaged gem with Ruby Policy 2.0

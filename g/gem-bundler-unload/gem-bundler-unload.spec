%define        _unpackaged_files_terminate_build 1
%define        gemname bundler-unload

Name:          gem-bundler-unload
Version:       1.0.2
Release:       alt1
Summary:       Allow unloading bundler after Bundler.load
License:       Apache 2.0
Group:         Development/Ruby
Url:           https://github.com/mpapis/bundler-unload
Vcs:           https://github.com/mpapis/bundler-unload.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(bundler) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(bundler-unload) = 1.0.2


%description
Allow unloading bundler after Bundler.load


%package       -n gem-bundler-unload-doc
Version:       1.0.2
Release:       alt1
Summary:       Allow unloading bundler after Bundler.load documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета bundler-unload
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(bundler-unload) = 1.0.2

%description   -n gem-bundler-unload-doc
Allow unloading bundler after Bundler.load documentation files.

%description   -n gem-bundler-unload-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета bundler-unload.


%package       -n gem-bundler-unload-devel
Version:       1.0.2
Release:       alt1
Summary:       Allow unloading bundler after Bundler.load development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета bundler-unload
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(bundler-unload) = 1.0.2
Requires:      gem(bundler) >= 0

%description   -n gem-bundler-unload-devel
Allow unloading bundler after Bundler.load development package.

%description   -n gem-bundler-unload-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета bundler-unload.


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

%files         -n gem-bundler-unload-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-bundler-unload-devel
%doc README.md


%changelog
* Wed Nov 22 2023 Pavel Skrylev <majioa@altlinux.org> 1.0.2-alt1
- + packaged gem with Ruby Policy 2.0

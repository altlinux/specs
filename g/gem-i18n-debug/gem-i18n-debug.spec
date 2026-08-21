%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname i18n-debug

Name:          gem-i18n-debug
Version:       1.2.0
Release:       alt1
Summary:       Ever wondered which translations are being looked up by Rails, a gem, or simply your app? Wonder no more!
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/fphilipe/i18n-debug
Vcs:           https://github.com/fphilipe/i18n-debug.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-ruby setup-rb rake
%if_enabled check
BuildRequires: gem(bundler) >= 1.7
BuildRequires: gem(minitest) >= 5.8
BuildRequires: gem(rake) >= 10.0
BuildConflicts: gem(bundler) >= 3
BuildConflicts: gem(i18n) >= 2
BuildConflicts: gem(minitest) >= 7
BuildConflicts: gem(rake) >= 14
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bundler >= 2.1.4,bundler < 3
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency minitest >= 6.0,minitest < 7
Conflicts:     gem(i18n) >= 2
Provides:      gem(i18n-debug) = 1.2.0

%description
Ever wondered which translations are being looked up by Rails, a gem, or simply
your app? Wonder no more!


%if_enabled    doc
%package       -n gem-i18n-debug-doc
Version:       1.2.0
Release:       alt1
Summary:       Ever wondered which translations are being looked up by Rails, a gem, or simply your app? Wonder no more! documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета i18n-debug
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(i18n-debug) = 1.2.0

%description   -n gem-i18n-debug-doc
Ever wondered which translations are being looked up by Rails, a gem, or simply
your app? Wonder no more! documentation files.

Ever wondered which translations are being looked up by Rails, a gem, or simply
your app? Wonder no more!

%description   -n gem-i18n-debug-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета i18n-debug.
%endif


%if_enabled    devel
%package       -n gem-i18n-debug-devel
Version:       1.2.0
Release:       alt1
Summary:       Ever wondered which translations are being looked up by Rails, a gem, or simply your app? Wonder no more! development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета i18n-debug
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(i18n-debug) = 1.2.0
Requires:      gem(bundler) >= 1.7
Requires:      gem(minitest) >= 5.8
Requires:      gem(rake) >= 10.0
Conflicts:     gem(bundler) >= 3
Conflicts:     gem(minitest) >= 7
Conflicts:     gem(rake) >= 14

%description   -n gem-i18n-debug-devel
Ever wondered which translations are being looked up by Rails, a gem, or simply
your app? Wonder no more! development package.

Ever wondered which translations are being looked up by Rails, a gem, or simply
your app? Wonder no more!

%description   -n gem-i18n-debug-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета i18n-debug.
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
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-i18n-debug-doc
%doc CHANGELOG.md LICENSE.txt README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-i18n-debug-devel
%doc CHANGELOG.md LICENSE.txt README.md
%endif


%changelog
* Fri Aug 21 2026 Pavel Skrylev <majioa@altlinux.org> 1.2.0-alt1
- + packaged gem with Ruby Policy 2.0
- * define explicit dependencies

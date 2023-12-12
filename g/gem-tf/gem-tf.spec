%define        _unpackaged_files_terminate_build 1
%define        gemname tf

Name:          gem-tf
Version:       0.4.5
Release:       alt1
Summary:       Testing Framework
License:       Apache-2.0
Group:         Development/Ruby
Url:           http://github.com/mpapis/tf
Vcs:           https://github.com/mpapis/tf.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(minitest) >= 5
BuildRequires: gem(session) >= 3.1
BuildConflicts: gem(minitest) >= 6
BuildConflicts: gem(session) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(session) >= 3.1
Conflicts:     gem(session) >= 4
Provides:      gem(tf) = 0.4.5

%ruby_bindir_to %ruby_bindir

%description
Testing Framework solely based on plugins. For now only tests using Bash.


%package       -n tf
Version:       0.4.5
Release:       alt1
Summary:       Testing Framework executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета tf
Group:         Other
BuildArch:     noarch

Requires:      gem(tf) = 0.4.5

%description   -n tf
Testing Framework executable(s).

Testing Framework solely based on plugins. For now only tests using Bash.

%description   -n tf -l ru_RU.UTF-8
Исполнямка для самоцвета tf.


%package       -n gem-tf-doc
Version:       0.4.5
Release:       alt1
Summary:       Testing Framework documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета tf
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(tf) = 0.4.5

%description   -n gem-tf-doc
Testing Framework documentation files.

Testing Framework solely based on plugins. For now only tests using Bash.

%description   -n gem-tf-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета tf.


%package       -n gem-tf-devel
Version:       0.4.5
Release:       alt1
Summary:       Testing Framework development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета tf
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(tf) = 0.4.5
Requires:      gem(minitest) >= 5
Conflicts:     gem(minitest) >= 6

%description   -n gem-tf-devel
Testing Framework development package.

Testing Framework solely based on plugins. For now only tests using Bash.

%description   -n gem-tf-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета tf.


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

%files         -n tf
%doc README.md
%ruby_bindir/tf

%files         -n gem-tf-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-tf-devel
%doc README.md


%changelog
* Wed Nov 22 2023 Pavel Skrylev <majioa@altlinux.org> 0.4.5-alt1
- + packaged gem with Ruby Policy 2.0

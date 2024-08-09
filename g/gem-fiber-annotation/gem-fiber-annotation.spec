%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname fiber-annotation

Name:          gem-fiber-annotation
Version:       0.2.0
Release:       alt1
Summary:       A mechanism for annotating fibers
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/ioquatix/fiber-annotation
Vcs:           https://github.com/ioquatix/fiber-annotation.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(fiber-annotation) = 0.2.0


%description
A mechanism for annotating fibers.


%if_enabled    doc
%package       -n gem-fiber-annotation-doc
Version:       0.2.0
Release:       alt1
Summary:       A mechanism for annotating fibers documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета fiber-annotation
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(fiber-annotation) = 0.2.0

%description   -n gem-fiber-annotation-doc
A mechanism for annotating fibers documentation files.

%description   -n gem-fiber-annotation-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета fiber-annotation.
%endif


%if_enabled    devel
%package       -n gem-fiber-annotation-devel
Version:       0.2.0
Release:       alt1
Summary:       A mechanism for annotating fibers development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета fiber-annotation
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(fiber-annotation) = 0.2.0

%description   -n gem-fiber-annotation-devel
A mechanism for annotating fibers development package.

%description   -n gem-fiber-annotation-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета fiber-annotation.
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
%doc readme.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-fiber-annotation-doc
%doc readme.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-fiber-annotation-devel
%doc readme.md
%endif


%changelog
* Wed Jul 24 2024 Pavel Skrylev <majioa@altlinux.org> 0.2.0-alt1
- + packaged gem with Ruby Policy 2.0

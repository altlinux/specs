# vim: set ft=spec: -*- rpm-spec -*-
%define        _unpackaged_files_terminate_build 1
%define        gemname unicode

Name:          gem-unicode
Version:       0.4.4.4
Release:       alt1.1
Summary:       Unicode normalization library
License:       Ruby
Group:         Development/Ruby
Url:           https://github.com/blackwinter/unicode
Vcs:           https://github.com/blackwinter/unicode.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(unicode) = 0.4.4.4

%ruby_use_gem_version unicode:0.4.4.4

%description
Unicode normalization library.


%package       -n gem-unicode-doc
Version:       0.4.4.4
Release:       alt1.1
Summary:       Unicode normalization library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета unicode
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(unicode) = 0.4.4.4

%description   -n gem-unicode-doc
Unicode normalization library documentation files.

%description   -n gem-unicode-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета unicode.


%package       -n gem-unicode-devel
Version:       0.4.4.4
Release:       alt1.1
Summary:       Unicode normalization library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета unicode
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(unicode) = 0.4.4.4

%description   -n gem-unicode-devel
Unicode normalization library development package.

%description   -n gem-unicode-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета unicode.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README
%ruby_gemspec
%ruby_gemlibdir
%ruby_gemextdir

%files         -n gem-unicode-doc
%doc README
%ruby_gemdocdir

%files         -n gem-unicode-devel
%doc README
%ruby_includedir/*


%changelog
* Wed Dec 06 2023 Pavel Skrylev <majioa@altlinux.org> 0.4.4.4-alt1.1
- ! fixed spec format

* Thu Dec 10 2020 Pavel Skrylev <majioa@altlinux.org> 0.4.4.4-alt1
- + packaged gem with usage Ruby Policy 2.0

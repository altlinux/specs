%define        gemname matrix

Name:          gem-matrix
Version:       0.4.2
Release:       alt1
Summary:       An implementation of Matrix and Vector classes
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/matrix
Vcs:           https://github.com/ruby/matrix.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(matrix) = 0.4.2


%description
An implementation of Matrix and Vector classes.


%package       -n gem-matrix-doc
Version:       0.4.2
Release:       alt1
Summary:       An implementation of Matrix and Vector classes documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета matrix
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(matrix) = 0.4.2

%description   -n gem-matrix-doc
An implementation of Matrix and Vector classes documentation files.

An implementation of Matrix and Vector classes.

%description   -n gem-matrix-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета matrix.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-matrix-doc
%ruby_gemdocdir


%changelog
* Mon Jun 28 2021 Pavel Skrylev <majioa@altlinux.org> 0.4.2-alt1
- + packaged gem with Ruby Policy 2.0

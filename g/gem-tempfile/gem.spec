%define        gemname tempfile

Name:          gem-tempfile
Version:       0.1.2
Release:       alt1
Summary:       A utility class for managing temporary files
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/tempfile
Vcs:           https://github.com/ruby/tempfile.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(tempfile) = 0.1.2


%description
A utility class for managing temporary files.


%package       -n gem-tempfile-doc
Version:       0.1.2
Release:       alt1
Summary:       A utility class for managing temporary files documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета tempfile
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(tempfile) = 0.1.2

%description   -n gem-tempfile-doc
A utility class for managing temporary files documentation files.

%description   -n gem-tempfile-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета tempfile.


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

%files         -n gem-tempfile-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Tue May 17 2022 Pavel Skrylev <majioa@altlinux.org> 0.1.2-alt1
- + packaged gem with Ruby Policy 2.0

%define        gemname forwardable

Name:          gem-forwardable
Version:       1.3.2
Release:       alt1
Summary:       Provides delegation of specified methods to a designated object
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/ruby/forwardable
Vcs:           https://github.com/ruby/forwardable.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(forwardable) = 1.3.2


%description
Provides delegation of specified methods to a designated object.


%package       -n gem-forwardable-doc
Version:       1.3.2
Release:       alt1
Summary:       Provides delegation of specified methods to a designated object documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета forwardable
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(forwardable) = 1.3.2

%description   -n gem-forwardable-doc
Provides delegation of specified methods to a designated object documentation
files.

%description   -n gem-forwardable-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета forwardable.


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

%files         -n gem-forwardable-doc
%ruby_gemdocdir


%changelog
* Tue Oct 04 2022 Pavel Skrylev <majioa@altlinux.org> 1.3.2-alt1
- + packaged gem with Ruby Policy 2.0

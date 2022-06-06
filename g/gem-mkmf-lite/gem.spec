%define        gemname mkmf-lite

Name:          gem-mkmf-lite
Version:       0.5.1
Release:       alt1
Summary:       A lighter version of mkmf designed for use as a library
License:       Apache-2.0
Group:         Development/Ruby
Url:           http://github.com/djberg96/mkmf-lite
Vcs:           https://github.com/djberg96/mkmf-lite.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(ptools) >= 1.4 gem(ptools) < 2
BuildRequires: gem(rspec) >= 3.9 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(ptools) >= 1.4 gem(ptools) < 2
Provides:      gem(mkmf-lite) = 0.5.1


%description
The mkmf-lite library is a light version of the the mkmf library designed for
use as a library. It does not create packages, builds, or log files of any kind.
Instead, it provides mixin methods that you can use in FFI or tests to check for
the presence of header files, constants, and so on.


%package       -n gem-mkmf-lite-doc
Version:       0.5.1
Release:       alt1
Summary:       A lighter version of mkmf designed for use as a library documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета mkmf-lite
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(mkmf-lite) = 0.5.1

%description   -n gem-mkmf-lite-doc
A lighter version of mkmf designed for use as a library documentation
files.

The mkmf-lite library is a light version of the the mkmf library designed for
use as a library. It does not create packages, builds, or log files of any kind.
Instead, it provides mixin methods that you can use in FFI or tests to check for
the presence of header files, constants, and so on.

%description   -n gem-mkmf-lite-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета mkmf-lite.


%package       -n gem-mkmf-lite-devel
Version:       0.5.1
Release:       alt1
Summary:       A lighter version of mkmf designed for use as a library development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета mkmf-lite
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(mkmf-lite) = 0.5.1
Requires:      gem(rspec) >= 3.9 gem(rspec) < 4

%description   -n gem-mkmf-lite-devel
A lighter version of mkmf designed for use as a library development
package.

The mkmf-lite library is a light version of the the mkmf library designed for
use as a library. It does not create packages, builds, or log files of any kind.
Instead, it provides mixin methods that you can use in FFI or tests to check for
the presence of header files, constants, and so on.

%description   -n gem-mkmf-lite-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета mkmf-lite.


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

%files         -n gem-mkmf-lite-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-mkmf-lite-devel
%doc README.md


%changelog
* Sun Apr 17 2022 Pavel Skrylev <majioa@altlinux.org> 0.5.1-alt1
- + packaged gem with Ruby Policy 2.0

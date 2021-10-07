%define        gemname ansi

Name:          gem-ansi
Version:       1.5.0
Release:       alt1.1
Summary:       Set of ANSI Code based classes and modules for Ruby
License:       BSD-2-Clause
Group:         Development/Ruby
Url:           http://rubyworks.github.io/ansi/
Vcs:           https://github.com/rubyworks/ansi.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(mast) >= 0
BuildRequires: gem(indexer) >= 0
# BuildRequires: gem(ergo) >= 0
BuildRequires: gem(qed) >= 0
BuildRequires: gem(ae) >= 0
BuildRequires: gem(lemon) >= 0

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(ansi) = 1.5.0


%description
The ANSI project is a collection of ANSI escape code related libraries enabling
ANSI code based colorization and stylization of output. It is very nice for
beautifying shell output.

This collection is based on a set of scripts spun-off from Ruby Facets. Included
are Code (used to be ANSICode), Logger, ProgressBar and String. In addition the
library includes Terminal which provides information about the current output
device.


%package       -n ansi
Version:       1.5.0
Release:       alt1.1
Summary:       Set of ANSI Code based classes and modules for Ruby executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета ansi
Group:         Other
BuildArch:     noarch

Requires:      gem(ansi) = 1.5.0

%description   -n ansi
Set of ANSI Code based classes and modules for Ruby executable(s).

The ANSI project is a collection of ANSI escape code related libraries enabling
ANSI code based colorization and stylization of output. It is very nice for
beautifying shell output.

This collection is based on a set of scripts spun-off from Ruby Facets. Included
are Code (used to be ANSICode), Logger, ProgressBar and String. In addition the
library includes Terminal which provides information about the current output
device.

%description   -n ansi -l ru_RU.UTF-8
Исполнямка для самоцвета ansi.


%package       -n gem-ansi-doc
Version:       1.5.0
Release:       alt1.1
Summary:       Set of ANSI Code based classes and modules for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ansi
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ansi) = 1.5.0

%description   -n gem-ansi-doc
Set of ANSI Code based classes and modules for Ruby documentation files.

The ANSI project is a collection of ANSI escape code related libraries enabling
ANSI code based colorization and stylization of output. It is very nice for
beautifying shell output.

This collection is based on a set of scripts spun-off from Ruby Facets. Included
are Code (used to be ANSICode), Logger, ProgressBar and String. In addition the
library includes Terminal which provides information about the current output
device.

%description   -n gem-ansi-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ansi.


%package       -n gem-ansi-devel
Version:       1.5.0
Release:       alt1.1
Summary:       Set of ANSI Code based classes and modules for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ansi
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ansi) = 1.5.0
Requires:      gem(mast) >= 0
Requires:      gem(indexer) >= 0
# Requires:      gem(ergo) >= 0
Requires:      gem(qed) >= 0
Requires:      gem(ae) >= 0
Requires:      gem(lemon) >= 0

%description   -n gem-ansi-devel
Set of ANSI Code based classes and modules for Ruby development package.

The ANSI project is a collection of ANSI escape code related libraries enabling
ANSI code based colorization and stylization of output. It is very nice for
beautifying shell output.

This collection is based on a set of scripts spun-off from Ruby Facets. Included
are Code (used to be ANSICode), Logger, ProgressBar and String. In addition the
library includes Terminal which provides information about the current output
device.

%description   -n gem-ansi-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ansi.


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

%files         -n ansi
%doc README.md

%files         -n gem-ansi-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-ansi-devel
%doc README.md


%changelog
* Wed Oct 06 2021 Pavel Skrylev <majioa@altlinux.org> 1.5.0-alt1.1
- ! spec

* Thu Jun 21 2019 Pavel Skrylev <majioa@altlinux.org> 1.5.0-alt1
- Initial build for Sisyphus, packaged as a gem with usage Ruby Policy 2.0.

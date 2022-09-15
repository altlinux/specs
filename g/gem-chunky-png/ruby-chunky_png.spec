%define        gemname chunky_png

Name:          gem-chunky-png
Version:       1.4.0
Release:       alt1
Summary:       Pure ruby library for read/write, chunk-level access to PNG files
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/wvanbergen/chunky_png
Vcs:           https://github.com/wvanbergen/chunky_png.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0
BuildRequires: gem(standard) >= 0
BuildRequires: gem(yard) >= 0.9 gem(yard) < 1
BuildRequires: gem(rspec) >= 3 gem(rspec) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-chunky_png < %EVR
Provides:      ruby-chunky_png = %EVR
Provides:      gem(chunky_png) = 1.4.0


%description
This pure Ruby library can read and write PNG images without depending on an
external image library, like RMagick. It tries to be memory efficient and
reasonably fast.

It supports reading and writing all PNG variants that are defined in the
specification, with one limitation: only 8-bit color depth is supported. It
supports all transparency, interlacing and filtering options the PNG
specifications allows. It can also read and write textual metadata from PNG
files. Low-level read/write access to PNG chunks is also possible.

This library supports simple drawing on the image canvas and simple operations
like alpha composition and cropping. Finally, it can import from and export to
RMagick for interoperability.


%package       -n gem-chunky-png-doc
Version:       1.4.0
Release:       alt1
Summary:       Pure ruby library for read/write, chunk-level access to PNG files documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета chunky_png
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(chunky_png) = 1.4.0

%description   -n gem-chunky-png-doc
Pure ruby library for read/write, chunk-level access to PNG files documentation
files.

This pure Ruby library can read and write PNG images without depending on an
external image library, like RMagick. It tries to be memory efficient and
reasonably fast.

It supports reading and writing all PNG variants that are defined in the
specification, with one limitation: only 8-bit color depth is supported. It
supports all transparency, interlacing and filtering options the PNG
specifications allows. It can also read and write textual metadata from PNG
files. Low-level read/write access to PNG chunks is also possible.

This library supports simple drawing on the image canvas and simple operations
like alpha composition and cropping. Finally, it can import from and export to
RMagick for interoperability.

%description   -n gem-chunky-png-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета chunky_png.


%package       -n gem-chunky-png-devel
Version:       1.4.0
Release:       alt1
Summary:       Pure ruby library for read/write, chunk-level access to PNG files development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета chunky_png
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(chunky_png) = 1.4.0
Requires:      gem(rake) >= 0
Requires:      gem(standard) >= 0
Requires:      gem(yard) >= 0.9 gem(yard) < 1
Requires:      gem(rspec) >= 3 gem(rspec) < 4

%description   -n gem-chunky-png-devel
Pure ruby library for read/write, chunk-level access to PNG files development
package.

This pure Ruby library can read and write PNG images without depending on an
external image library, like RMagick. It tries to be memory efficient and
reasonably fast.

It supports reading and writing all PNG variants that are defined in the
specification, with one limitation: only 8-bit color depth is supported. It
supports all transparency, interlacing and filtering options the PNG
specifications allows. It can also read and write textual metadata from PNG
files. Low-level read/write access to PNG chunks is also possible.

This library supports simple drawing on the image canvas and simple operations
like alpha composition and cropping. Finally, it can import from and export to
RMagick for interoperability.

%description   -n gem-chunky-png-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета chunky_png.


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

%files         -n gem-chunky-png-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-chunky-png-devel
%doc README.md


%changelog
* Tue Aug 23 2022 Pavel Skrylev <majioa@altlinux.org> 1.4.0-alt1
- ^ 1.3.11 -> 1.4.0

* Mon Feb 03 2020 Alexey Shabalin <shaba@altlinux.org> 1.3.11-alt1
- Initial build.

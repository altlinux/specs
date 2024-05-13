%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname msgpack

Name:          gem-msgpack
Version:       1.7.2
Release:       alt1
Summary:       MessagePack implementation for Ruby
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/msgpack/msgpack-ruby
Vcs:           https://github.com/msgpack/msgpack-ruby.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>

Source:        %name-%version.tar
Patch:         license.patch
BuildRequires(pre): rpm-build-ruby
%if_enabled check
BuildRequires: gem(bundler) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rake-compiler) >= 1.1.2
BuildRequires: gem(rspec) >= 3.3
BuildRequires: gem(ruby_memcheck) >= 0
BuildRequires: gem(yard) >= 0
BuildRequires: gem(json) >= 0
BuildRequires: gem(benchmark-ips) >= 2.10.0
BuildRequires: gem(rubocop) >= 0.82.0
BuildRequires: gem(simplecov) >= 0
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(benchmark-ips) >= 2.11
BuildConflicts: gem(rubocop) >= 2
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rubocop >= 1.15.0,rubocop < 2
%ruby_use_gem_dependency rake-compiler >= 1.1.2,rake-compiler < 2
Obsoletes:     ruby-msgpack < %EVR
Provides:      ruby-msgpack = %EVR
Provides:      gem(msgpack) = 1.7.2


%description
MessagePack is an efficient binary serialization format. It lets you exchange
data among multiple languages like JSON but it's faster and smaller. For
example, small integers (like flags or error code) are encoded into a single
byte, and typical short strings only require an extra byte in addition to the
strings themselves.

If you ever wished to use JSON for convenience (storing an image with metadata)
but could not for technical reasons (binary data, size, speed ...), MessagePack
is a perfect replacement.


%if_enabled    doc
%package       -n gem-msgpack-doc
Version:       1.7.2
Release:       alt1
Summary:       MessagePack implementation for Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета msgpack
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(msgpack) = 1.7.2
Obsoletes:     msgpack-doc
Provides:      msgpack-doc

%description   -n gem-msgpack-doc
MessagePack implementation for Ruby documentation files.

MessagePack is an efficient binary serialization format. It lets you exchange
data among multiple languages like JSON but it's faster and smaller. For
example, small integers (like flags or error code) are encoded into a single
byte, and typical short strings only require an extra byte in addition to the
strings themselves.

If you ever wished to use JSON for convenience (storing an image with metadata)
but could not for technical reasons (binary data, size, speed ...), MessagePack
is a perfect replacement.

%description   -n gem-msgpack-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета msgpack.
%endif


%if_enabled    devel
%package       -n gem-msgpack-devel
Version:       1.7.2
Release:       alt1
Summary:       MessagePack implementation for Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета msgpack
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(msgpack) = 1.7.2
Requires:      gem(bundler) >= 0
Requires:      gem(rake) >= 0
Requires:      gem(rake-compiler) >= 1.1.2
Requires:      gem(rspec) >= 3.3
Requires:      gem(ruby_memcheck) >= 0
Requires:      gem(yard) >= 0
Requires:      gem(json) >= 0
Requires:      gem(benchmark-ips) >= 2.10.0
Requires:      gem(rubocop) >= 0.82.0
Requires:      gem(simplecov) >= 0
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(benchmark-ips) >= 2.11
Conflicts:     gem(rubocop) >= 2
Conflicts:     libmsgpack-devel

%description   -n gem-msgpack-devel
MessagePack implementation for Ruby development package.

MessagePack is an efficient binary serialization format. It lets you exchange
data among multiple languages like JSON but it's faster and smaller. For
example, small integers (like flags or error code) are encoded into a single
byte, and typical short strings only require an extra byte in addition to the
strings themselves.

If you ever wished to use JSON for convenience (storing an image with metadata)
but could not for technical reasons (binary data, size, speed ...), MessagePack
is a perfect replacement.

%description   -n gem-msgpack-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета msgpack.
%endif


%prep
%setup
%autopatch

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
%ruby_gemextdir

%if_enabled    doc
%files         -n gem-msgpack-doc
%doc README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-msgpack-devel
%doc README.md
%ruby_includedir/*
%endif


%changelog
* Wed May 08 2024 Pavel Skrylev <majioa@altlinux.org> 1.7.2-alt1
- ^ 1.5.6 -> 1.7.2
- * relicensed

* Wed Sep 21 2022 Pavel Skrylev <majioa@altlinux.org> 1.5.6-alt1
- ^ 1.4.5 -> 1.5.6

* Thu Mar 17 2022 Pavel Skrylev <majioa@altlinux.org> 1.4.5-alt1
- ^ 1.3.3 -> 1.4.5

* Thu Mar 05 2020 Pavel Skrylev <majioa@altlinux.org> 1.3.3-alt1
- updated (^) 1.3.1 -> 1.3.3
- fixed (!) spec

* Mon Sep 16 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.1-alt1
- updated (^) 1.2.9 -> 1.3.1
- fixed (!) spec

* Tue Apr 16 2019 Pavel Skrylev <majioa@altlinux.org> 1.2.9-alt1
- used (>) Ruby Policy 2.0
- updated (^) 1.1.0 -> 1.2.9

* Sun Sep 30 2018 Mikhail Gordeev <obirvalger@altlinux.org> 1.1.0-alt1.5
- Add rubygem files

* Fri Mar 30 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1.4
- Rebuild with Ruby 2.5.1

* Tue Mar 13 2018 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1.3
- Rebuild with Ruby 2.5.0

* Mon Sep 25 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1.2
- Rebuild with Ruby 2.4.2

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.1.0-alt1.1
- Rebuild with Ruby 2.4.1

* Mon May 15 2017 Gordeev Mikhail <obirvalger@altlinux.org> 1.1.0-alt1
- Initial build in Sisyphus

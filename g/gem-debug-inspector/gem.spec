%define        gemname debug_inspector

Name:          gem-debug-inspector
Version:       1.1.0
Release:       alt1
Summary:       A Ruby wrapper for the MRI 2.0 debug_inspector API
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/banister/debug_inspector
Vcs:           https://github.com/banister/debug_inspector.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(debug_inspector) = 1.1.0


%description
Adds methods to RubyVM::DebugInspector to allow for inspection of backtrace
frames.

The debug_inspector C extension and API were designed and built by Koichi
Sasada, this project is just a gemification of his work.

This library makes use of the debug inspector API which was added to MRI 2.0.0.
Only works on MRI 2 and 3. Requiring it on unsupported Rubies will result in a
no-op.

Recommended for use only in debugging situations. Do not use this in production
apps.


%package       -n gem-debug-inspector-doc
Version:       1.1.0
Release:       alt1
Summary:       A Ruby wrapper for the MRI 2.0 debug_inspector API documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета debug_inspector
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(debug_inspector) = 1.1.0

%description   -n gem-debug-inspector-doc
A Ruby wrapper for the MRI 2.0 debug_inspector API documentation files.

Adds methods to RubyVM::DebugInspector to allow for inspection of backtrace
frames.

The debug_inspector C extension and API were designed and built by Koichi
Sasada, this project is just a gemification of his work.

This library makes use of the debug inspector API which was added to MRI 2.0.0.
Only works on MRI 2 and 3. Requiring it on unsupported Rubies will result in a
no-op.

Recommended for use only in debugging situations. Do not use this in production
apps.

%description   -n gem-debug-inspector-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета debug_inspector.


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
%ruby_gemextdir

%files         -n gem-debug-inspector-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Fri Jun 04 2021 Pavel Skrylev <majioa@altlinux.org> 1.1.0-alt1
- + packaged gem with Ruby Policy 2.0

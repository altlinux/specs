%define        _unpackaged_files_terminate_build 1
%def_enable    check
%def_enable    doc
%def_enable    devel
%define        gemname binding_of_caller

Name:          gem-binding-of-caller
Version:       1.0.1
Release:       alt1
Summary:       Retrieve the binding of a method's caller, or further up the stack
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/banister/binding_of_caller
Vcs:           https://github.com/banister/binding_of_caller.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(rake) >= 0
%if_enabled check
BuildRequires: gem(debug_inspector) >= 1.2.0
BuildRequires: gem(rspec) >= 0
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_alias_names binding_of_caller,binding-of-caller
Requires:      ruby >= 2.0.0
Requires:      gem(debug_inspector) >= 1.2.0
Provides:      binding_of_caller = %EVR
Provides:      gem(binding_of_caller) = 1.0.1

%description
Provides the Binding#of_caller method.

Using binding_of_caller we can grab bindings from higher up the call stack and
evaluate code in that context. Allows access to bindings arbitrarily far up the
call stack, not limited to just the immediate caller.

Recommended for use only in debugging situations. Do not use this in production
apps.


%if_enabled    doc
%package       -n gem-binding-of-caller-doc
Version:       1.0.1
Release:       alt1
Summary:       Retrieve the binding of a method's caller, or further up the stack documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета binding_of_caller
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(binding_of_caller) = 1.0.1

%description   -n gem-binding-of-caller-doc
Retrieve the binding of a method's caller, or further up the stack documentation
files.

Provides the Binding#of_caller method.

Using binding_of_caller we can grab bindings from higher up the call stack and
evaluate code in that context. Allows access to bindings arbitrarily far up the
call stack, not limited to just the immediate caller.

Recommended for use only in debugging situations. Do not use this in production
apps.

%description   -n gem-binding-of-caller-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета binding_of_caller.
%endif


%if_enabled    devel
%package       -n gem-binding-of-caller-devel
Version:       1.0.1
Release:       alt1
Summary:       Retrieve the binding of a method's caller, or further up the stack development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета binding_of_caller
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(binding_of_caller) = 1.0.1
Requires:      gem(rake) >= 0
Requires:      gem(rspec) >= 0

%description   -n gem-binding-of-caller-devel
Retrieve the binding of a method's caller, or further up the stack development
package.

Provides the Binding#of_caller method.

Using binding_of_caller we can grab bindings from higher up the call stack and
evaluate code in that context. Allows access to bindings arbitrarily far up the
call stack, not limited to just the immediate caller.

Recommended for use only in debugging situations. Do not use this in production
apps.

%description   -n gem-binding-of-caller-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета binding_of_caller.
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
%doc LICENSE README.md
%ruby_gemspec
%ruby_gemlibdir

%if_enabled    doc
%files         -n gem-binding-of-caller-doc
%doc LICENSE README.md
%ruby_gemdocdir
%endif

%if_enabled    devel
%files         -n gem-binding-of-caller-devel
%doc LICENSE README.md
%endif


%changelog
* Tue Jan 21 2025 Pavel Skrylev <majioa@altlinux.org> 1.0.1-alt1
- ^ 1.0.0 -> 1.0.1

* Fri Jun 04 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- + packaged gem with Ruby Policy 2.0

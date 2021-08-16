%define        gemname binding_of_caller

Name:          gem-binding-of-caller
Version:       1.0.0
Release:       alt1
Summary:       Retrieve the binding of a method's caller, or further up the stack
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/banister/binding_of_caller
Vcs:           https://github.com/banister/binding_of_caller.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(debug_inspector) >= 0.0.1

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Requires:      gem(debug_inspector) >= 0.0.1
Provides:      gem(binding_of_caller) = 1.0.0


%description
Provides the Binding#of_caller method.

Using binding_of_caller we can grab bindings from higher up the call stack and
evaluate code in that context. Allows access to bindings arbitrarily far up the
call stack, not limited to just the immediate caller.

Recommended for use only in debugging situations. Do not use this in production
apps.


%package       -n gem-binding-of-caller-doc
Version:       1.0.0
Release:       alt1
Summary:       Retrieve the binding of a method's caller, or further up the stack documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета binding_of_caller
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(binding_of_caller) = 1.0.0

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


%package       -n gem-binding-of-caller-devel
Version:       1.0.0
Release:       alt1
Summary:       Retrieve the binding of a method's caller, or further up the stack development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета binding_of_caller
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(binding_of_caller) = 1.0.0

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

%files         -n gem-binding-of-caller-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-binding-of-caller-devel
%doc README.md


%changelog
* Fri Jun 04 2021 Pavel Skrylev <majioa@altlinux.org> 1.0.0-alt1
- + packaged gem with Ruby Policy 2.0

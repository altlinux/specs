# For offline build
%global _zig_project_options %_zig_project_options -Dversion_data_path=%_docdir/zig/langref.html.in

%global _zig_cache_dir %_builddir/zig-cache

Name:     zls
Version:  0.13.0
Release:  alt1
Summary:  A Zig language server supporting Zig developers with features like autocomplete and goto definition

License:  MIT
Group:    Development/Other
URL:      https://github.com/zigtools/zls

Source0:  %name-%version.tar
Source1:  vendor.tar

ExclusiveArch: %zig_arches

BuildRequires(pre): rpm-macros-zig
BuildRequires: zig

%description
The Zig Language Server (ZLS) is a tool that implements Microsoft's
Language Server Protocol for Zig in Zig. In simpler terms: it'll provide
you with completions, go-to definition, etc. when you write Zig code!

%prep
%setup -a1
mv ./vendor %_zig_cache_dir

%build
%zig_build

%install
%zig_install

%check
%zig_test

%files
%doc README.md LICENSE
%_bindir/zls

%changelog
* Fri Oct 04 2024 Ilya Sorochan <k0tran@altlinux.org> 0.13.0-alt1
- Initial build for ALT Linux.

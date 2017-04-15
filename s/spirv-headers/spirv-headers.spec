%define commit db5cf6176137003ca4c25df96f7c0649998c3499

Name: spirv-headers
Version: 1.1
Release: alt1

Summary: Machine-readable files from the SPIR-V registry
License: MIT
Group: Development/C++

Url: https://www.khronos.org/registry/spir-v/
Packager: Nazarov Denis <nenderus@altlinux.org>
BuildArch: noarch

Source: https://github.com/KhronosGroup/SPIRV-Headers/archive/%commit/SPIRV-Headers-%commit.tar.gz

%description
This package contains machine-readable files from the SPIR-V
registry. This includes:

* Header files for various languages.
* JSON files describing the grammar for the SPIR-V core instruction
  set, and for the GLSL.std.450 extended instruction set.
* The XML registry file.

%prep
%setup -n SPIRV-Headers-%commit

%install
%__mkdir_p %buildroot%_includedir
%__cp -a include/spirv %buildroot%_includedir/spirv

%files
%doc LICENSE README.md
%_includedir/spirv

%changelog
* Sat Apr 15 2017 Nazarov Denis <nenderus@altlinux.org> 1.1-alt1
- Initial release for ALT Linux

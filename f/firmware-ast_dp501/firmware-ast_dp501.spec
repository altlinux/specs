Name: firmware-ast_dp501
Version: 0.99.08
Release: alt1

Summary: Firmware for ASPEED AST2400
License: proprietary
Group: System/Kernel and hardware

Url: http://www.supermicro.com/support/faqs/faq.cfm?faq=26876
# http://drive.google.com/file/d/1rBp3z_4_LNmx8ci_U4VAL5-qB4sjM-aV/view?usp=sharing ->
# http://drive.google.com/uc?id=1rBp3z_4_LNmx8ci_U4VAL5-qB4sjM-aV&export=download
# version as found in the binary
Source0: ast_dp501_fw.bin
Source1: README.ALT

BuildArch: noarch
AutoReqProv: no

%description
%summary provided by Supermicro.

%prep

%install
install -pDm644 %SOURCE0 %buildroot/lib/firmware/ast_dp501_fw.bin
install -pDm644 %SOURCE1 README.ALT

%files
/lib/firmware/ast_dp501_fw.bin
%doc README.ALT

%changelog
* Thu Oct 28 2021 Michael Shigorin <mike@altlinux.org> 0.99.08-alt1
- initial release;
  see also http://forum.altlinux.org/index.php?topic=41530.15

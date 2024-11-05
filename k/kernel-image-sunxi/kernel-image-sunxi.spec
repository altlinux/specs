%def_disable check
%def_disable docs
%def_disable domU

Name: kernel-image-sunxi
Release: alt1

%define kernel_base_version	6.6
%define kernel_sublevel	.54
%define kernel_extra_version	%nil
Version: %kernel_base_version%kernel_sublevel%kernel_extra_version

%define krelease	%release

%define flavour		%( s='%name'; printf %%s "${s#kernel-image-}" )
%define base_flavour	%( s='%flavour'; printf %%s "${s%%%%-*}" )
%define sub_flavour	%( s='%flavour'; printf %%s "${s#*-}" )

# Build options
# You can change compiler version by editing this line:
%define kgcc_version	%__gcc_version_base

#Remove oss
%def_disable oss
## Don't edit below this line ##################################

%define kversion	%kernel_base_version%kernel_sublevel%kernel_extra_version
%define modules_dir	/lib/modules/%kversion-%flavour-%krelease

%define kheaders_dir	%_prefix/include/linux-%kversion-%flavour
%define kbuild_dir	%_prefix/src/linux-%kversion-%flavour-%krelease
%define old_kbuild_dir	%_prefix/src/linux-%kversion-%flavour

%brp_strip_none /boot/*
%add_verify_elf_skiplist %modules_dir/*

Summary: The Linux kernel (the core of the Linux operating system)
License: GPL-2.0-only
Group: System/Kernel and hardware
Url: http://www.kernel.org/
Packager: Kernel Maintainers Team <kernel@packages.altlinux.org>

Source1: config-aarch64

Patch0000: linux-%version.patch

# Sort oreder patches https://github.com/armbian/build/blob/main/patch/kernel/archive/sunxi-6.6/series.conf
Patch0001: mailbox-Allow-to-run-mailbox-while-timekeeping-is-suspended.patch
Patch0002: ARM-sunxi-Add-experimental-suspend-to-memory-implementation-for.patch
Patch0003: ARM-sunxi-sunxi_cpu0_hotplug_support_set-is-not-supported-on-A8.patch
Patch0004: firmware-scpi-Add-support-for-sending-a-SCPI_CMD_SET_SYS_PWR_ST.patch
Patch0005: ARM-sunxi-Use-SCPI-to-send-suspend-message-to-SCP-on-A83T.patch
Patch0006: gnss-ubx-Send-soft-powerdown-message-on-suspend.patch
Patch0007: dt-bindings-vendor-prefix-add-prefix-for-Voltafield.patch
Patch0008: dt-bindings-iio-magnetometer-add-DT-binding-for-Voltafield-AF81.patch
Patch0009: MAINTAINERS-add-an-entry-for-AF8133J-driver.patch
Patch0010: iio-magnetometer-add-a-driver-for-Voltafield-AF8133J-magnetomet.patch
Patch0011: iio-af8133j-Cleanup-probe-and-power-up-down.patch
Patch0012: iio-af8133j-Add-runtime-power-management.patch
Patch0013: iio-af8133j-Add-support-for-buffer.patch
Patch0014: iio-af8133j-Avoid-compiler-warning.patch
Patch0015: phy-allwinner-sun4i-usb-Add-support-for-usb_role_switch.patch
Patch0016: regulator-axp20x-Add-support-for-vin-supply-for-drivevbus.patch
Patch0017: regulator-axp20x-Turn-N_VBUSEN-to-input-on-x-powers-sense-vbus-.patch
Patch0018: drm-bridge-dw-hdmi-Allow-to-accept-HPD-status-from-other-driver.patch
Patch0019: drm-bridge-dw-hdmi-Report-HDMI-hotplug-events.patch
Patch0020: usb-typec-anx7688-Add-driver-for-ANX7688-USB-C-HDMI-bridge.patch
Patch0021: usb-typec-anx7688-Don-t-use-I2C-regulator.patch
Patch0022: usb-typec-anx7688-I2C-bus-power-needs-to-be-enabled.patch
Patch0023: ASOC-sun9i-hdmi-audio-Initial-implementation.patch
Patch0024: ARM-dts-sunxi-h3-h5-Add-hdmi-sound-card.patch
Patch0025: ARM-dts-sun8i-h3-Enable-hdmi-sound-card-on-boards-with-hdmi.patch
Patch0026: ARM-dts-sun8i-h2-plus-bananapi-m2-zero-Enable-HDMI-audio.patch
Patch0027: ARM-dts-sun8i-a83t-Add-hdmi-sound-card.patch
Patch0028: ARM-dts-sun8i-a83t-Enable-hdmi-sound-card-on-boards-with-hdmi.patch
Patch0029: ARM-dts-sun8i-r40-Add-hdmi-sound-card.patch
Patch0030: ARM-dts-sun8i-r40-bananapi-m2-ultra-Enable-HDMI-audio.patch
Patch0031: ARM-dts-sun8i-v40-bananapi-m2-berry-Enable-HDMI-audio.patch
Patch0032: arm64-dts-allwinner-h6-Add-hdmi-sound-card.patch
Patch0033: arm64-dts-allwinner-h6-Enable-hdmi-sound-card-on-boards-with-hd.patch
Patch0034: arm64-dts-allwinner-a64-Add-hdmi-sound-card.patch
Patch0035: arm64-dts-allwinner-a64-Enable-hdmi-sound-card-on-boards-with-h.patch
Patch0036: arm64-dts-allwinner-h5-Enable-hdmi-sound-card-on-boards-with-hd.patch
Patch0037: ASoC-sun50i-codec-analog-Add-support-for-internal-bias.patch
Patch0038: ASoC-sun50i-codec-analog-Move-suspend-resume-to-set_bias_level.patch
Patch0039: ASoC-sun50i-codec-analog-Enable-jack-detection-on-startup.patch
Patch0040: ASoC-sun8i-codec-Enable-bus-clock-at-STANDBY-and-higher-bias.patch
Patch0041: ASoC-sun8i-codec-Implement-jack-and-accessory-detection.patch
Patch0042: ASoC-ec25-New-codec-driver-for-the-EC25-modem.patch
Patch0043: clk-sunxi-ng-a64-Increase-PLL_AUDIO-base-frequency.patch
Patch0044: sound-soc-sun8i-codec-Add-support-for-digital-part-of-the-AC100.patch
Patch0045: sound-soc-sun8i-codec-Drop-debug-statements.patch
Patch0046: sound-soc-ac100-codec-Support-analog-part-of-X-Powers-AC100-cod.patch
Patch0047: sound-soc-ac100-Make-sure-we-shutdown-the-audio-outputs-on-rebo.patch
Patch0048: ASoC-sunxi-sun8i-codec-Improve-jack-button-handling-and-mic-det.patch
Patch0049: dt-bindings-axp20x-adc-allow-to-use-TS-pin-as-GPADC.patch
Patch0050: iio-adc-axp20x_adc-allow-to-set-TS-pin-to-GPADC-mode.patch
Patch0051: power-axp20x_battery-Allow-to-set-target-voltage-to-4.35V.patch
Patch0052: power-supply-axp20x_battery-Add-support-for-reporting-OCV.patch
Patch0053: regulator-axp20x-Enable-over-temperature-protection-and-16s-res.patch
Patch0054: power-supply-axp20x_battery-Setup-thermal-regulation-experiment.patch
Patch0055: power-supply-axp20x_battery-Fix-charging-done-detection.patch
Patch0056: mfd-axp20x-Add-battery-IRQ-resources.patch
Patch0057: power-supply-axp20x_battery-Send-uevents-for-status-changes.patch
Patch0058: power-supply-axp20x_battery-Monitor-battery-health.patch
Patch0059: power-supply-axp20x-usb-power-Change-Vbus-hold-voltage-to-4.5V.patch
Patch0060: power-axp803-Add-interrupts-for-low-battery-power-condition.patch
Patch0061: power-supply-axp20x-battery-Support-POWER_SUPPLY_PROP_CHARGE_BE.patch
Patch0062: power-supply-axp20x-battery-Enable-poweron-by-RTC-alarm.patch
Patch0063: power-supply-axp20x-battery-Add-support-for-POWER_SUPPLY_PROP_E.patch
Patch0064: power-supply-Add-support-for-USB_BC_ENABLED-and-USB_DCP_INPUT_C.patch
Patch0065: power-supply-axp20x-usb-power-Support-input-current-limit-expor.patch
Patch0066: dt-bindings-media-Add-bindings-for-Himax-HM5065-camera-sensor.patch
Patch0067: hm5065-yaml-bindings-wip.patch
Patch0068: media-hm5065-Add-subdev-driver-for-Himax-HM5065-camera-sensor.patch
Patch0069: MAINTAINERS-Add-entry-for-Himax-HM5065.patch
Patch0070: media-gc2145-Galaxycore-camera-module-driver.patch
Patch0071: media-gc2145-Added-BGGR-bayer-mode.patch
Patch0072: media-gc2145-Disable-debug-output.patch
Patch0073: media-gc2145-Add-PIXEL_RATE-HBLANK-and-VBLANK-controls.patch
Patch0074: media-ov5640-Experiment-Try-to-disable-denoising-sharpening.patch
Patch0075: media-ov5640-Sleep-after-poweroff-to-ensure-next-poweron-is-not.patch
Patch0076: media-ov5640-Don-t-powerup-the-sensor-during-driver-probe.patch
Patch0077: media-ov5640-set-default-ae-target-lower.patch
Patch0078: media-ov5640-Improve-error-reporting.patch
Patch0079: media-ov5640-Implement-autofocus.patch
Patch0080: media-ov5640-Improve-firmware-load-time.patch
Patch0081: media-ov5640-Fix-focus-commands-blocking-until-complete.patch
Patch0082: media-ov5640-Add-read-only-property-for-vblank.patch
Patch0083: media-sun6i-csi-capture-Use-subdev-operation-to-access-bridge-f.patch
Patch0084: media-sun6i-csi-subdev-Use-subdev-active-state-to-store-active-.patch
Patch0085: media-sun6i-csi-merge-sun6i_csi_formats-and-sun6i_csi_formats_m.patch
Patch0086: media-sun6i-csi-add-V4L2_CAP_IO_MC-capability.patch
Patch0087: media-sun6i-csi-implement-vidioc_enum_framesizes.patch
Patch0088: media-sun6i-csi-Add-multicamera-support-for-parallel-bus.patch
Patch0089: media-gc2145-implement-system-suspend.patch
Patch0090: media-ov5640-use-pm_runtime_force_suspend-resume-for-system-sus.patch
Patch0091: media-gc2145-fix-white-balance-colors.patch
Patch0092: drm-sun4i-Unify-sun8i_-_layer-structs.patch
Patch0093: drm-sun4i-Add-more-parameters-to-sunxi_engine-commit-callback.patch
Patch0094: drm-sun4i-Fix-layer-zpos-change-atomic-modesetting.patch
Patch0095: drm-sun4i-Implement-gamma-correction.patch
Patch0096: drm-panel-st7703-Improve-the-power-up-down-sequence-of-the-pane.patch
Patch0097: drm-panel-st7703-Fix-xbd599-timings-to-make-refresh-rate-exactl.patch
Patch0098: drm-sun4i-Support-taking-over-display-pipeline-state-from-p-boo.patch
Patch0099: video-pwm_bl-Allow-to-change-lth_brightness-via-sysfs.patch
Patch0100: clk-sunxi-ng-add-support-for-rate-resetting-notifier.patch
Patch0101: clk-sunxi-ng-a64-keep-tcon0-clock-rate-when-pll-video0-s-rate-c.patch
Patch0102: drm-sun4i-tcon-hand-over-the-duty-to-keep-TCON0-clock-to-CCU-on.patch
Patch0103: clk-sunxi-ng-sun50i-a64-Switch-parent-of-MIPI-DSI-to-periph0-1x.patch
Patch0104: sunxi-Use-dev_err_probe-to-handle-EPROBE_DEFER-errors.patch
Patch0105: thermal-sun8i-Be-loud-when-probe-fails.patch
Patch0106: i2c-mv64xxx-Don-t-make-a-fuss-when-pinctrl-recovery-state-is-no.patch
Patch0107: iio-st_sensors-Don-t-report-error-when-the-device-is-not-presen.patch
Patch0108: opp-core-Avoid-confusing-error-when-no-regulator-is-defined-in-.patch
Patch0109: media-cedrus-Fix-failure-to-clean-up-hardware-on-probe-failure.patch
Patch0110: Revert-drm-sun4i-lvds-Invert-the-LVDS-polarity.patch
Patch0111: arm64-dts-allwinner-Enforce-consistent-MMC-numbering.patch
Patch0112: ARM-dts-sunxi-Add-aliases-for-MMC.patch
Patch0113: of-property-fw_devlink-Support-allwinner-sram-links.patch
Patch0114: ARM-dts-sun8i-a83t-Add-missing-GPU-trip-point.patch
Patch0115: arm64-dts-sun50i-h5-Add-missing-GPU-trip-point.patch
Patch0116: Fix-intptr_t-typedef.patch
Patch0117: usb-gadget-Fix-dangling-pointer-in-netdev-private-data.patch
Patch0118: clk-sunxi-ng-Export-CLK_DRAM-for-devfreq.patch
Patch0119: ARM-dts-sun8i-a83t-Add-MBUS-node.patch
Patch0120: usb-quirks-Add-USB_QUIRK_RESET-for-Quectel-EG25G-Modem.patch
Patch0121: misc-modem-power-Power-manager-for-modems.patch
Patch0122: net-stmmac-sun8i-Use-devm_regulator_get-for-PHY-regulator.patch
Patch0123: net-stmmac-sun8i-Rename-PHY-regulator-variable-to-regulator_phy.patch
Patch0124: net-stmmac-sun8i-Add-support-for-enabling-a-regulator-for-PHY-I.patch
Patch0125: arm64-dts-allwinner-orange-pi-3-Enable-ethernet.patch
Patch0126: iio-adc-sun4i-gpadc-iio-Allow-to-use-sun5i-a13-gpadc-iio-from-D.patch
Patch0127: mtd-spi-nor-Add-regulator-support.patch
Patch0128: input-cyttsp4-De-obfuscate-platform-data-for-keys.patch
Patch0129: input-cyttsp4-Remove-useless-indirection-with-driver-platform-d.patch
Patch0130: input-cyttsp4-Remove-unused-enable_vkeys.patch
Patch0131: input-cyttsp4-De-obfuscate-MT-signals-setup-platform-data.patch
Patch0132: input-cyttsp4-Clear-the-ids-buffer-in-a-saner-way.patch
Patch0133: input-cyttsp4-ENOSYS-error-is-ok-when-powering-up.patch
Patch0134: input-cyttsp4-Faster-recovery-from-failed-wakeup-HACK.patch
Patch0135: input-cyttsp4-Use-i2c-spi-names-directly-in-the-driver.patch
Patch0136: input-cyttsp4-Port-the-driver-to-use-device-properties.patch
Patch0137: input-cyttsp4-Restart-on-wakeup-wakeup-by-I2C-read-doesn-t-work.patch
Patch0138: input-cyttsp4-Fix-warnings.patch
Patch0139: input-cyttsp4-Make-the-driver-not-hog-the-system-s-workqueue.patch
Patch0140: regulator-Add-simple-driver-for-enabling-a-regulator-from-users.patch
Patch0141: regulator-tp65185x-Add-tp65185x-eInk-panel-regulator-driver.patch
Patch0142: regulator-tp65185-Add-hwmon-device-for-reading-temperature.patch
Patch0143: ARM-dts-sun5i-Add-soc-handle.patch
Patch0144: ARM-dts-sun5i-Add-PocketBook-Touch-Lux-3-display-ctp-support.patch
Patch0145: ARM-dts-sun5i-a13-pocketbook-touch-lux-3-Add-RTC-clock-cells.patch
Patch0146: mfd-sun4i-gpadc-Interrupt-numbers-should-start-from-1.patch
Patch0147: input-cyttsp4-Fix-probe-oops.patch
Patch0148: arm64-dts-allwinner-a64-pinetab-add-front-camera.patch
Patch0149: arm64-allwinner-dts-a64-enable-K101-IM2BYL02-panel-for-PineTab.patch
Patch0150: iio-core-Add-option-to-force-identity-mount-matrix.patch
Patch0151: input-touchscreen-goodix-Add-config-debugfs-file.patch
Patch0152: input-goodix-Add-option-to-power-off-the-controller-during-susp.patch
Patch0153: arm64-dts-allwinner-a64-Fix-LRADC-compatible.patch
Patch0154: arm64-dts-sun50i-a64-pinephone-Add-front-back-cameras.patch
Patch0155: arm64-dts-sun50i-a64-pinephone-Add-Type-C-support-for-all-PP-va.patch
Patch0156: arm64-dts-sun50i-a64-pinephone-Add-modem-power-manager.patch
Patch0157: arm64-dts-sun50i-a64-pinephone-Fix-BH-modem-manager-behavior.patch
Patch0158: arm64-dts-sun50i-a64-pinephone-Add-detailed-OCV-to-capactiy-con.patch
Patch0159: arm64-dts-sun50i-a64-pinephone-Shorten-post-power-on-delay-on-m.patch
Patch0160: arm64-dts-sun50i-a64-pinephone-Add-mount-matrix-for-acceleromet.patch
Patch0161: arm64-dts-sun50i-a64-pinephone-Add-support-for-Bluetooth-audio.patch
Patch0162: arm64-dts-sun50i-a64-pinephone-Enable-internal-HMIC-bias.patch
Patch0163: arm64-dts-sun50i-a64-pinephone-Add-support-for-modem-audio.patch
Patch0164: arm64-dts-sun50i-a64-pinephone-Retain-leds-state-in-suspend.patch
Patch0165: arm64-dts-sun50i-a64-pinephone-Bump-I2C-frequency-to-400kHz.patch
Patch0166: arm64-dts-sun50i-a64-pinephone-Add-interrupt-pin-for-WiFi.patch
Patch0167: arm64-dts-sun50i-a64-pinephone-Power-off-the-touch-controller-i.patch
Patch0168: arm64-dts-sun50i-a64-pinephone-Don-t-make-lradc-keys-a-wakeup-s.patch
Patch0169: arm64-dts-sun50i-a64-pinephone-Set-minimum-backlight-duty-cycle.patch
Patch0170: arm64-dts-sun50i-a64-pinephone-Add-supply-for-i2c-bus-to-anx768.patch
Patch0171: arm64-dts-sun50i-a64-pinephone-Workaround-broken-HDMI-HPD-signa.patch
Patch0172: arm64-dts-sun50i-a64-pinephone-Add-AF8133J-to-PinePhone.patch
Patch0173: arm64-dts-sun50i-a64-pinephone-Add-mount-matrix-for-PinePhone-m.patch
Patch0174: arm64-dts-sun50i-a64-pinephone-Add-support-for-Pinephone-keyboa.patch
Patch0175: arm64-dts-sun50i-a64-pinephone-Enable-Pinephone-Keyboard-power-.patch
Patch0176: arm64-dts-sun50i-a64-Add-missing-trip-points-for-GPU.patch
Patch0177: arm64-dts-allwinner-sun50i-a64-pinephone-Add-support-for-Pineph.patch
Patch0178: iio-stk3310-Implement-vdd-supply-and-power-it-off-during-suspen.patch
Patch0179: iio-light-stk3310-Add-support-for-I2C-regulator.patch
Patch0180: input-touch-goodix-Try-to-keep-regulator-enable-disable-balance.patch
Patch0181: ARM-dts-allwinner-sun50i-64-pinephone-Add-power-supply-to-stk33.patch
Patch0182: power-supply-ip5xxx-Report-remaining-battery-capacity.patch
Patch0183: power-supply-ip5xxx-Modify-initial-configuration.patch
Patch0184: power-supply-ip5xxx-Add-boost-status-property.patch
Patch0185: power-supply-ip5xxx-Add-ip5xxx-usb-supply.patch
Patch0186: power-supply-ip5xxx-Add-support-for-POWER_SUPPLY_PROP_CHARGE_BE.patch
Patch0187: power-supply-ip5xxx-Add-support-for-POWER_SUPPLY_PROP_ENERGY_FU.patch
Patch0188: input-pinephone-keyboard-Allow-disabling-the-keyboard-input.patch
Patch0189: input-pinephone-keyboard-Allow-to-disable-Fn-layer-processing.patch
Patch0190: input-pinephone-keyboard-Don-t-print-error-when-the-keyboard-is.patch
Patch0191: misc-ppkb-manager-Pinephone-Keyboard-power-manager.patch
Patch0192: input-pinephone-keyboard-Wait-a-bit-after-enabling-vbus.patch
Patch0193: misc-ppkb-manager-Remove-BLOCKED-flag.patch
Patch0194: misc-ppkb-manager-Disable-ppkb-manager-by-default-can-be-enable.patch
Patch0195: misc-ppkb-manager-Show-read-write-error-codes.patch
Patch0196: misc-ppkb-manager-Disable-debug-mode.patch
Patch0197: clk-Implement-protected-clocks-for-all-OF-clock-providers.patch
Patch0198: Revert-clk-qcom-Support-protected-clocks-property.patch
Patch0199: ARM-dts-sunxi-a83t-Protect-SCP-clocks.patch
Patch0200: ARM-dts-sunxi-h3-h5-Protect-SCP-clocks.patch
Patch0201: arm64-dts-allwinner-a64-Protect-SCP-clocks.patch
Patch0202: arm64-dts-allwinner-h6-Protect-SCP-clocks.patch
Patch0203: bus-sunxi-rsb-Always-check-register-address-validity.patch
Patch0204: firmware-arm_scpi-Support-unidirectional-mailbox-channels.patch
Patch0205: ARM-dts-sunxi-a83t-Add-SCPI-protocol.patch
Patch0206: ARM-dts-sunxi-h3-h5-Add-SCPI-protocol.patch
Patch0207: arm64-dts-allwinner-a64-Add-SCPI-protocol.patch
Patch0208: arm64-dts-allwinner-h6-Add-SCPI-protocol.patch
Patch0209: ARM-dts-sun8i-a83t-tbs-a711-Give-Linux-more-privileges-over-SCP.patch
Patch0210: rtc-sun6i-Allow-RTC-wakeup-after-shutdown.patch
Patch0211: mmc-sunxi-mmc-Remove-runtime-PM.patch
Patch0212: arm64-dts-pinephone-Add-reboot-mode-driver.patch
Patch0213: arm64-dts-sun50i-a64-Set-fifo-size-for-uarts.patch
Patch0214: ARM-dts-sun8i-a83t-Set-fifo-size-for-uarts.patch
Patch0215: Mark-some-slow-drivers-for-async-probe-with-PROBE_PREFER_ASYNCH.patch
Patch0216: arm64-xor-Select-32regs-without-benchmark-to-speed-up-boot.patch
Patch0217: dt-bindings-leds-Add-a-binding-for-AXP813-charger-led.patch
Patch0218: leds-axp20x-Support-charger-LED-on-AXP20x-like-PMICs.patch
Patch0219: ARM-dts-axp813-Add-charger-LED.patch
Patch0220: ARM-dts-sun8i-a83t-tbs-a711-Enable-charging-LED.patch
Patch0221: nfc-pn544-Add-support-for-VBAT-PVDD-regulators.patch
Patch0222: bluetooth-bcm-Restore-drive_rts_on_open-true-behavior-on-bcm207.patch
Patch0223: mmc-add-delay-after-power-class-selection.patch
Patch0224: dt-bindings-input-gpio-vibrator-Don-t-require-enable-gpios.patch
Patch0225: input-gpio-vibra-Allow-to-use-vcc-supply-alone-to-control-the-v.patch
Patch0226: ARM-dts-sun8i-a83t-tbs-a711-Add-support-for-the-vibrator-motor.patch
Patch0227: ARM-dts-sun8i-a83t-tbs-a711-Increase-voltage-on-the-vibrator.patch
Patch0228: ARM-dts-sun8i-a83t-tbs-a711-Add-PN544-NFC-support.patch
Patch0229: ARM-dts-sun8i-a83t-tbs-a711-Add-powerup-down-support-for-the-3G.patch
Patch0230: ARM-dts-sun8i-a83t-Add-cedrus-video-codec-support-to-A83T-untes.patch
Patch0231: ARM-dts-suni-a83t-Add-i2s0-pins.patch
Patch0232: ARM-dts-sun8i-a83t-tbs-a711-Add-sound-support-via-AC100-codec.patch
Patch0233: ARM-dts-sun8i-a83t-tbs-a711-Add-regulators-to-the-accelerometer.patch
Patch0234: ARM-dts-sun8i-a83t-tbs-a711-Add-camera-sensors-HM5065-GC2145.patch
Patch0235: ARM-dts-sun8i-a83t-tbs-a711-Add-flash-led-support.patch
Patch0236: clk-sunxi-ng-Set-maximum-P-and-M-factors-to-1-for-H3-pll-cpux-c.patch
Patch0237: clk-sunxi-ng-Don-t-use-CPU-PLL-gating-and-CPUX-reparenting-to-H.patch
Patch0238: ARM-dts-sun8i-h3-Use-my-own-more-aggressive-OPPs-on-H3.patch
Patch0239: arm64-dts-sun50i-h5-Use-my-own-more-aggressive-OPPs-on-H5.patch
Patch0240: ARM-dts-sun8i-h3-orange-pi-pc-Increase-max-CPUX-voltage-to-1.4V.patch
Patch0241: ARM-dts-sun8i-a83t-Improve-CPU-OPP-tables-go-up-to-1.8GHz.patch
Patch0242: cpufreq-sun50i-Show-detected-CPU-bin-for-easier-debugging.patch
Patch0243: Fix-warning-multi-line-comment.patch
Patch0244: Fix-duplicate-nodes-for-sun50i-h5-orangepi-pc2.patch
Patch0245: Doc-dt-bindings-usb-add-binding-for-DWC3-controller-on-Allwinne.patch
Patch0246: drv-pinctrl-pinctrl-sun50i-a64-disable_strict_mode.patch
Patch0247: drv-rtc-sun6i-support-RTCs-without-external-LOSCs.patch
Patch0248: drv-gpu-drm-gem-dma-Export-with-handle-allocator.patch
Patch0249: drv-gpu-drm-sun4i-Add-GEM-allocator.patch
Patch0250: drv-gpu-drm-sun4i-Add-HDMI-audio-sun4i-hdmi-encoder.patch
Patch0251: drv-net-stmmac-dwmac-sun8i-second-EMAC-clock-register.patch
Patch0252: drv-phy-sun4i-usb-Allow-reset-line-to-be-shared.patch
Patch0253: drv-iio-adc-sun4i-gpadc-iio-rename-A33-specified-registers-to-c.patch
Patch0254: drv-iio-adc-sun4i-gpadc-iio-sampling-start-end-code-readout-reg.patch
Patch0255: drv-iio-adc-sun4i-gpadc-iio-support-clocks-and-reset.patch
Patch0256: drv-iio-adc-sun4i-gpadc-iio-multible-sensors-support.patch
Patch0257: drv-iio-adc-sun4i-gpadc-iio-support-nvmem-calibration-data.patch
Patch0258: drv-iio-adc-sun4i-gpadc-iio-add-interrupt-support.patch
Patch0259: drv-iio-adc-sun4i-gpadc-iio-add-H3-thermal-sensor.patch
Patch0260: drv-iio-adc-sun4i-gpadc-iio-add-A83T-thermal-sensor.patch
Patch0261: drv-iio-adc-Kconfig-enable-A80-A64-H5-for-THS.patch
Patch0262: drv-iio-adc-sun4i-gpadc-iio-add-A80-thermal-sensor.patch
Patch0263: drv-iio-adc-sun4i-gpadc-iio-add-A64-thermal-sensor.patch
Patch0264: drv-iio-sun4i-gpadc-iio-don-t-force-poweroff.patch
Patch0265: drv-staging-media-sunxi-cedrus-add-H616-variant.patch
Patch0266: drv-soc-sunxi-sram-Add-SRAM-C1-H616-handling.patch
Patch0267: drv-media-dvb-frontends-si2168-fix-cmd-timeout.patch
Patch0268: include-uapi-drm_fourcc-add-ARM-tiled-format-modifier.patch
Patch0269: drv-clk-sunxi-ng-ccu-add-min-max-rate-sun50i-a64.patch
Patch0270: drv-clocksource-arm_arch_timer-fix-a64-timejump.patch
Patch0271: sound-soc-sunxi-sun4i-spdif-add-mclk_multiplier.patch
Patch0272: sound-soc-sunxi-sun8i-codec-analog-enable-sound.patch
Patch0273: sound-soc-sunxi-Provoke-the-early-load-of-sun8i-codec-analog.patch
Patch0274: sound-soc-sunxi-sun4i-codec-adcis-select-capture-source.patch
Patch0275: drv-mmc-host-sunxi-mmc-add-h5-emmc-compatible.patch
Patch0276: drv-pinctrl-sunxi-pinctrl-sun50i-h6.c-GPIO-disable_strict_mode.patch
Patch0277: drv-gpu-drm-sun4i-sun8i_mixer.c-add-h3-mixer1.patch
Patch0278: drv-mtd-nand-raw-nand_ids.c-add-H27UBG8T2BTR-BC-nand.patch
Patch0279: drv-mfd-axp20x-add-sysfs-interface.patch
Patch0280: drv-spi-spidev-Add-armbian-spi-dev-compatible.patch
Patch0281: drv-spi-spi-sun4i.c-spi-bug-low-on-sck.patch
Patch0282: drv-rtc-sun6i-Add-Allwinner-H616-support.patch
Patch0283: drv-nvmem-sunxi_sid-Support-SID-on-H616.patch
Patch0284: drv-thermal-sun8i_thermal-Add-for-H616.patch
Patch0285: drv-iio-adc-axp20x_adc-arm64-dts-axp803-hwmon-enable-thermal.patch
Patch0286: drv-gpu-drm-panel-simple-Add-compability-olinuxino-lcd.patch
Patch0287: drv-input-touchscreen-sun4i-ts-Enable-parsing.patch
Patch0288: drv-mmc-host-sunxi-mmc-Disable-DDR52-mode-on-all-A20-based-boar.patch
Patch0289: drv-usb-gadget-composite-rename-gadget-serial-console-manufactu.patch
Patch0290: arm-arm64-dts-Add-leds-axp20x-charger.patch
Patch0291: arm-dts-sun9i-a80-add-thermal-sensor.patch
Patch0292: arm-dts-sun9i-a80-add-thermal-zone.patch
Patch0293: arm-dts-sun7i-a20-Disable-OOB-IRQ-for-brcm-wifi-on-Cubietruck-a.patch
Patch0294: arm-dts-a20-orangepi-and-mini-fix-phy-mode-hdmi.patch
Patch0295: arm-dts-sun8i-h3-nanopi-add-leds-pio-pins.patch
Patch0296: arm-dts-a10-cubiebord-a20-cubietruck-green-LED-mmc0-default-tri.patch
Patch0297: arm-dts-Add-sun8i-h2-plus-nanopi-duo-device.patch
Patch0298: arm-dts-Add-sun8i-h2-plus-sunvell-r69-device.patch
Patch0299: arm-dts-h3-nanopi-neo-Add-regulator-leds-mmc2.patch
Patch0300: arm-dts-h3-nanopi-neo-air-Add-regulator-camera-wifi-bluetooth-o.patch
Patch0301: arm-dts-h3-orangepi-2-Add-regulator-vdd-cpu.patch
Patch0302: arm-dts-sun8i-r40-bananapi-m2-ultra-add-codec-analog.patch
Patch0303: arm-dts-sun7i-a20-cubietruck-add-alias-uart2.patch
Patch0304: arm-dts-sun8i-v3s-s3-pinecube-enable-sound-codec.patch
Patch0305: arm-dts-sun8i-r40-add-clk_out_a-fix-bananam2ultra.patch
Patch0306: arm-dts-sun8i-h3-bananapi-m2-plus-add-wifi_pwrseq.patch
Patch0307: arm-dts-sun7i-a20-bananapro-add-hdmi-connector-de.patch
Patch0308: Bananapro-add-AXP209-regulators.patch
Patch0309: arm-dts-sunxi-h3-h5.dtsi-force-mmc0-bus-width.patch
Patch0310: arm64-dts-sun50i-a64-pine64-enable-wifi-mmc1.patch
Patch0311: arm64-dts-sun50i-a64-sopine-baseboard-Add-i2s2-mmc1.patch
Patch0312: arm64-dts-sun50i-h6-Add-r_uart-uart2-3-pins.patch
Patch0313: arm64-dts-allwiner-sun50i-h616.dtsi-add-usb-ehci-ohci.patch
Patch0314: arm64-dts-sun50i-h616-orangepi-zero2-reg_usb1_vbus-status-ok.patch
Patch0315: arm64-dts-allwinner-sun50i-h616-Add-GPU-node.patch
Patch0316: arm64-dts-sun50i-h616-orangepi-zero2-Enable-GPU-mali.patch
Patch0317: arm64-dts-allwinner-sun50i-h616-Add-VPU-node.patch
Patch0318: arm64-dts-sun50i-h616-x96-mate-T95-eth-sd-card-hack.patch
Patch0319: arm64-dts-sun50i-h616-x96-mate-add-hdmi.patch
Patch0320: arm64-dts-sun50i-h313-x96q-lpddr3.patch
Patch0321: arm64-dts-allwinner-h616-Add-device-node-for-SID.patch
Patch0322: arm64-dts-allwinner-h616-Add-efuse_xlate-cpu-frequency-scaling-.patch
Patch0323: arm64-dts-allwinner-h616-Add-thermal-sensor-and-thermal-zones.patch
Patch0324: arm64-dts-allwinner-h616-Fix-thermal-zones-add-missing-trips.patch
Patch0325: Add-FB_TFT-ST7796S-driver.patch
Patch0326: Optimize-TSC2007-touchscreen-add-polling-method.patch
Patch0327: Add-ws2812-RGB-driver-for-allwinner-H616.patch
Patch0328: LED-green_power_on-red_status_heartbeat-arch-arm64-boot-dts-all.patch
Patch0329: arm64-dts-allwinner-h616-orangepi-zero2-Enable-expansion-board-.patch
Patch0330: arm64-dts-sun50i-a64-pine64-enable-Bluetooth.patch
Patch0331: arm64-dts-sun50i-a64-sopine-baseboard-enable-Bluetooth.patch
Patch0332: arm64-dts-nanopi-a64-set-right-phy-mode-to-rgmii-id.patch
Patch0333: arm64-dts-FIXME-a64-olinuxino-add-regulator-audio-mmc.patch
Patch0334: arm64-dts-Add-sun50i-h5-nanopi-k1-plus-device.patch
Patch0335: arm64-dts-Add-sun50i-h5-nanopi-neo-core2-device.patch
Patch0336: arm64-dts-Add-sun50i-h5-nanopi-neo2-v1.1-device.patch
Patch0337: arm64-dts-Add-sun50i-h5-nanopi-m1-plus2-device.patch
Patch0338: arm64-dts-sun50i-h5-nanopi-neo2-add-regulator-led-triger.patch
Patch0339: arm64-dts-sun50i-h5-orangepi-pc2-add-spi-flash.patch
Patch0340: arm64-dts-sun50i-h5-orangepi-prime-add-regulator.patch
Patch0341: arm64-dts-sun50i-h5-orangepi-zero-plus-add-regulator.patch
Patch0342: arm64-dts-sun50i-h5-orangepi-zero-plus2-regulator-gpio-fix.patch
Patch0343: arm64-dts-sun50i-h6.dtsi-improve-thermals.patch
Patch0344: arm64-dts-sun50i-h6-orangepi-3-delete-node-spi0.patch
Patch0345: arm64-dts-sun50i-h6-orangepi-lite2-spi0-usb3phy-dwc3-enable.patch
Patch0346: arm64-dts-sun50i-h6-pine-h64-add-wifi-rtl8723cs.patch
Patch0347: arm64-dts-sun50i-h6-pine-h64-add-dwc3-usb3phy.patch
Patch0348: arm64-dts-sun50i-a64-pine64-add-spi0.patch
Patch0349: arm64-dts-sun50i-h6.dtsi-add-pinctrl-pins-for-spi.patch
Patch0350: arm64-dts-sun50i-a64-orangepi-win-add-aliase-ethernet1.patch
Patch0351: arm64-dts-sun50i-a64-force-mmc0-bus-width.patch
Patch0352: drv-of-Device-Tree-Overlay-ConfigFS-interface.patch
Patch0353: scripts-add-overlay-compilation-support.patch
Patch0354: scripts-enable-kernel-dtbs-symbol-generation.patch
Patch0355: Makefile-CONFIG_SHELL-fix-for-builddeb-packaging.patch
Patch0356: arm-dts-overlay-Add-Overlays-for-sunxi.patch
Patch0357: arm64-dts-allwinner-overlay-Add-Overlays-for-sunxi64.patch
Patch0358: arm-dts-overlay-sun8i-h3-cpu-clock-add-overclock.patch
Patch0359: arm64-dts-overlay-sun50i-a64-pine64-7inch-lcd.patch
Patch0360: arm64-dts-overlay-sun50i-h5-add-gpio-regulator-overclock.patch
Patch0361: Move-sun50i-h6-pwm-settings-to-its-own-overlay.patch
Patch0362: Compile-the-pwm-overlay.patch
Patch0363: cb1-overlay.patch
Patch0364: ARM64-DTS-sun50i-h616-overlays-fix-sun50i-h616-light-overlay.patch
Patch0365: arm-dts-sunxi-h3-h5.dtsi-add-i2s0-i2s1-pins.patch
Patch0366: arm-dts-sun5i-a13-olinuxino-micro-add-panel-lcd-olinuxino-4.3.patch
Patch0367: arm-dts-sun5i-a13-olinuxino-Add-panel-lcd-olinuxino-4.3-needed-.patch
Patch0368: arm-dts-sun7i-a20-olinuxino-micro-emmc-Add-vqmmc-node.patch
Patch0369: arm-dts-sun7i-a20-olinuxino-lime2-enable-audio-codec.patch
Patch0370: arm-dts-sun7i-a20-olinuxino-lime2-enable-ldo3-always-on.patch
Patch0371: arm-dts-sun7i-a20-olimex-som-204-evb-olinuxino-micro-decrease-d.patch
Patch0372: arm-dts-sun8i-h3-add-thermal-zones.patch
Patch0373: arm64-dts-sun50i-a64-olinuxino-add-boards.patch
Patch0374: arm64-dts-sun50i-a64-olinuxino-emmc-enable-bluetooth.patch
Patch0375: arm64-dts-sun50i-a64-olinuxino-1Ge16GW-enable-bluetooth.patch
Patch0376: arm64-dts-sun50i-a64.dtsi-adjust-thermal-trip-points.patch
Patch0377: arm64-dts-sun50i-a64-olinuxino-1Ge16GW-Disable-clock-phase-and-.patch
Patch0378: Temp_fix-mailbox-arch-arm64-boot-dts-allwinner-sun50i-a64-pinep.patch
Patch0379: arm64-dts-sun50i-h6-orangepi-3-add-r_uart-aliase.patch
Patch0380: arm64-dts-sun50i-h5-add-cpu-opp-refs.patch
Patch0381: arm64-dts-sun50i-h5-add-termal-zones.patch
Patch0382: arm64-dts-sun50i-h6-orangepi-add-cpu-opp-refs.patch
Patch0383: arm64-dts-sun50i-h6-orangepi-enable-higher-clock-regulator-max-.patch
Patch0384: drv-staging-rtl8723bs-AP-bugfix.patch
Patch0385: arm-dts-sun8i-h3-orangepi-pc-plus-add-wifi_pwrseq.patch
Patch0386: arm64-dts-sun50i-h5-orangepi-prime-add-rtl8723cs.patch
Patch0387: arm-dts-sun8i-h2-plus-orangepi-zero-fix-xradio-interrupt.patch
Patch0388: Fix-include-uapi-spi-spidev-module.patch
Patch0389: fix-cpu-opp-table-sun8i-a83t.patch
Patch0390: Add-dump_reg-and-sunxi-sysinfo-drivers.patch
Patch0391: Add-sunxi-addr-driver-Used-to-fix-uwe5622-bluetooth-MAC-address.patch
Patch0392: nvmem-sunxi_sid-add-sunxi_get_soc_chipid-sunxi_get_serial.patch
Patch0393: mmc-host-sunxi-mmc-Fix-H6-emmc.patch
Patch0394: arm64-dts-allwinner-sun50i-h6-Fix-H6-emmc.patch
Patch0395: arm64-dts-sun50i-h5-nanopi-r1s-h5-add-rtl8153-support.patch
Patch0396: net-usb-r8152-add-LED-configuration-from-OF.patch
Patch0397: arm64-dts-sun50i-h6-orangepi.dtsi-Rollback-r_rsb-to-r_i2c.patch
Patch0398: add-bigtreetech-cb1-dts.patch
Patch0399: Add-board-BananaPi-BPI-M4-ZERO.patch
Patch0400: ARM-dts-sun8i-nanopiduo2-Use-key-0-as-power-button.patch
Patch0401: ARM-dts-sun8i-nanopiduo2-enable-ethernet.patch
Patch0402: arm-dts-sun8i-h3-reduce-opp-microvolt-to-prevent-not-supported-.patch
Patch0403: arm64-dts-sun50i-h5-enable-power-button-for-orangepi-prime.patch
Patch0404: enable-TV-Output-on-OrangePi-Zero-LTE.patch
Patch0405: drivers-devfreq-sun8i-a33-mbus-disable-autorefresh.patch
Patch0406: clk-gate-add-support-for-regmap-based-gates.patch
Patch0407: mfd-Add-support-for-X-Powers-AC200.patch
Patch0408: mfd-Add-support-for-X-Powers-AC200-EPHY-syscon.patch
Patch0409: net-phy-Add-support-for-AC200-EPHY.patch
Patch0410: arm64-dts-allwinner-h6-Add-AC200-EPHY-nodes.patch
Patch0411: arm64-dts-allwinner-h6-tanix-enable-Ethernet.patch
Patch0412: ASoC-AC200-Initial-driver.patch
Patch0413: arm64-dts-allwinner-h6-add-AC200-codec-nodes.patch
Patch0414: arm64-dts-allwinner-h6-enable-AC200-codec.patch
Patch0415: add-nodes-for-sunxi-info-sunxi-addr-and-sunxi-dump-reg.patch
Patch0416: add-initial-support-for-orangepi3-lts.patch
Patch0417: Input-axp20x-pek-allow-wakeup-after-shutdown.patch
Patch0418: Add-wifi-nodes-for-Inovato-Quadra.patch
Patch0419: arm64-dts-h616-add-wifi-support-for-orange-pi-zero-2-and-zero3.patch
Patch0420: arm64-dts-sun50i-h618-orangepi-zero3-Enable-GPU-mali.patch
Patch0421: drivers-hack-for-h616-hdmi-video-output.patch
Patch0422: arm64-dts-h616-add-hdmi-support-for-zero2-and-zero3.patch
Patch0423: arm64-dts-sun50i-h616-Add-dma-node.patch
Patch0424: arm64-dts-H616-Add-overlays-that-are-also-compatible-with-orang.patch
Patch0425: drivers-pwm-Add-pwm-sunxi-enhance-driver-for-h616.patch
Patch0426: driver-allwinner-h618-emac.patch
Patch0427: orangepi-zero2w-add-dtb.patch
Patch0428: arm64-dts-sun50i-h616-bananapi-m4-i2c-spi1-uart-pins.patch
Patch0429: add-dtb-overlay-for-zero2w.patch
Patch0430: Add-BPI-M4-ZERO-sdio-wifi-bt-overlay.patch
Patch0431: adding-dummy-regulators-in-pinctr-arch-arm-boot-dts-allwinner-s.patch
Patch0432: Sound-for-H616-H618-Allwinner-SOCs.patch
Patch0433: ARM64-dts-sun50i-h616-BigTreeTech-CB1-Enable-HDMI.patch
Patch0434: ARM64-dts-sun50i-h616-BigTreeTech-CB1-Enable-EMAC1.patch
Patch0435: ARM64-dts-sun50i-h616-BigTreeTech-CB1-Enable-IR-receiver.patch
Patch0436: arm64-dts-sun50i-h618-cherryba-m1.patch

ExclusiveArch: aarch64

%define make_target Image
%define image_path arch/%base_arch/boot/%make_target
%define arch_dir %base_arch
%define kvm_modules_dir arch/%arch_dir/kvm
%define qemu_pkg %_arch

ExclusiveOS: Linux

Requires(pre,postun): bootloader-utils
Requires(pre,postun): kmod
Requires(pre,postun): mkinitrd

BuildRequires(pre): rpm-build-kernel
BuildRequires: banner
BuildRequires: bc
BuildRequires: dwarves >= 1.16
BuildRequires: flex
BuildRequires: gcc%kgcc_version
BuildRequires: gcc%kgcc_version-c++
BuildRequires: gcc%kgcc_version-plugin-devel
BuildRequires: kernel-source-%kernel_base_version
BuildRequires: kmod
BuildRequires: libdb4-devel
BuildRequires: libelf-devel
BuildRequires: libgmp-devel
BuildRequires: libmpc-devel
BuildRequires: lzma-utils
BuildRequires: module-init-tools
BuildRequires: openssl
BuildRequires: openssl-devel
BuildRequires: rsync
BuildRequires: zlib-devel
BuildRequires: u-boot-tools
%if_with cross_toolchain_aarch64
BuildRequires: gcc-aarch64-linux-gnu
%endif

# for check
%{?!_without_check:%{?!_disable_check:BuildRequires: qemu-system-%qemu_pkg-core ipxe-roms-qemu glibc-devel-static}}

%if_enabled docs
BuildRequires: python3-module-sphinx /usr/bin/sphinx-build perl-Pod-Usage python3-module-sphinx_rtd_theme
BuildRequires: fontconfig
%endif

%if_enabled ccache
BuildRequires: ccache
%endif

%ifdef use_ccache
BuildRequires: ccache
%endif

%description
This package contains the Linux kernel %kernel_base_version that is used to boot and run
your system.

Most hardware drivers for this kernel are built as modules.  Some of
these drivers are built separately from the kernel; they are available
in separate packages (kernel-modules-*-%flavour).

There are some other kernel variants in ALT systems:
* std-def: latest longterm (LTS) kernel;
* un-def:  latest stable kernel, usually higher version than std-def.

%package -n kernel-image-domU-%flavour
Summary: Uncompressed linux kernel for XEN domU boot 
Group: System/Kernel and hardware
Requires(pre): coreutils
Requires(pre): module-init-tools >= 3.1

%description -n kernel-image-domU-%flavour
Most XEN virtualization system versions can not boot lzma-compressed
kernel images. This is an optional package with uncompressed linux
kernel image for this special case. If you do not know what is it XEN
it seems that you do not need this package.

%package -n kernel-headers-%flavour
Summary: Header files for the Linux kernel
Group: Development/Kernel
Requires: kernel-headers-common
Provides: kernel-headers = %version

%description -n kernel-headers-%flavour
This package makes Linux kernel headers corresponding to the Linux
kernel package %name-%version-%release available for building
userspace programs (if this version of headers is selected by
adjust_kernel_headers).

Since Linux 2.6.18 the kernel build system supports creation of
sanitized kernel headers for use in userspace (by deleting headers
which are not usable in userspace and removing #ifdef __KERNEL__
blocks from installed headers).  This package contains sanitized
headers instead of raw kernel headers which were present in some
previous versions of similar packages.

If possible, try to use glibc-kernheaders instead of this package.

%package -n kernel-headers-modules-%flavour
Summary: Headers and other files needed for building kernel modules
Group: Development/Kernel 
Requires: gcc%kgcc_version

%description -n kernel-headers-modules-%flavour
This package contains header files, Makefiles and other parts of the
Linux kernel build system which are needed to build kernel modules for
the Linux kernel package %name-%version-%release.

If you need to compile a third-party kernel module for the Linux
kernel package %name-%version-%release, install this package
and specify %kbuild_dir as the kernel source
directory.

%prep
%setup -cT -n kernel-image-%flavour-%kversion-%krelease
rm -rf kernel-source-%kernel_base_version
tar -xf %kernel_src/kernel-source-%kernel_base_version.tar
%setup -D -T -n kernel-image-%flavour-%kversion-%krelease/kernel-source-%kernel_base_version
%define _default_patch_flags -s
%autopatch -p1

cp %SOURCE1 .

# this file should be usable both with make and sh (for broken modules
# which do not use the kernel makefile system)
echo 'export GCC_VERSION=%kgcc_version' > gcc_version.inc

subst 's/EXTRAVERSION[[:space:]]*=.*/EXTRAVERSION = %kernel_extra_version-%flavour-%krelease/g' Makefile
%if_without cross_toolchain_aarch64
subst 's/CC.*$(CROSS_COMPILE)gcc/CC         := $(shell echo $${GCC_USE_CCACHE:+ccache}) gcc-%kgcc_version/g' Makefile
%endif

# get rid of unwanted files resulting from patch fuzz
find . -name "*.orig" -delete -or -name "*~" -delete

%if 0%{?_is_ilp32}
sed -Ei 's/-j[[:digit:]]*/-j8/' scripts/pahole-flags.sh
%endif

%build
banner build
export ARCH=%base_arch
export NPROCS=%__nprocs
%if_with cross_toolchain_aarch64
export CROSS_COMPILE=aarch64-linux-gnu-
%endif
KernelVer=%kversion-%flavour-%krelease

echo "Building Kernel $KernelVer"

%make_build mrproper

#configuration construction

CONFIGS="config-%_target_cpu"

scripts/kconfig/merge_config.sh -m $CONFIGS

%make_build oldconfig
%make_build %make_target
%make_build modules
%make_build dtbs

echo "Kernel built $KernelVer"

%if_enabled docs
# psdocs, pdfdocs don't work yet
%make_build htmldocs
%endif

%install
banner install
export ARCH=%base_arch
KernelVer=%kversion-%flavour-%krelease

install -Dp -m644 System.map %buildroot/boot/System.map-$KernelVer
install -Dp -m644 %image_path %buildroot/boot/vmlinuz-$KernelVer
%if_enabled domU
install -Dp -m644 vmlinux %buildroot/boot/vmlinux-$KernelVer
%endif
install -Dp -m644 .config %buildroot/boot/config-$KernelVer

%make_build modules_install INSTALL_MOD_PATH=%buildroot

make dtbs_install INSTALL_DTBS_PATH=%buildroot/boot/devicetree/$KernelVer

pushd %buildroot/boot/devicetree/$KernelVer
find . -mindepth 2 -name "*.dtb" | \
       while read f; do ln -srv "$f" "$(basename $f)"; done
popd

mkdir -p %buildroot%kbuild_dir/arch/%arch_dir
install -d %buildroot%kbuild_dir
cp -a include %buildroot%kbuild_dir/include
cp -a arch/%arch_dir/include %buildroot%kbuild_dir/arch/%arch_dir
# Delete CONFIG_ files and stray .cmds
find %buildroot%kbuild_dir/include/config -name '[0-9A-Z]*' -delete
find %buildroot%kbuild_dir -name '*.cmd' -delete

# drivers-headers install
install -d %buildroot%kbuild_dir/drivers/scsi
install -d %buildroot%kbuild_dir/drivers/md
install -d %buildroot%kbuild_dir/drivers/usb/core
install -d %buildroot%kbuild_dir/drivers/net/wireless
install -d %buildroot%kbuild_dir/net/mac80211
install -d %buildroot%kbuild_dir/kernel
install -d %buildroot%kbuild_dir/lib
cp -a drivers/md/dm*.h \
	%buildroot%kbuild_dir/drivers/md/
cp -a drivers/usb/core/*.h \
	%buildroot%kbuild_dir/drivers/usb/core/
cp -a drivers/net/wireless/Kconfig \
	%buildroot%kbuild_dir/drivers/net/wireless/
cp -a lib/hexdump.c %buildroot%kbuild_dir/lib/
cp -a kernel/workqueue.c %buildroot%kbuild_dir/kernel/
cp -a net/mac80211/ieee80211_i.h \
	%buildroot%kbuild_dir/net/mac80211/
cp -a net/mac80211/sta_info.h \
	%buildroot%kbuild_dir/net/mac80211/

# Remove -Werror from Makefile for external modules
sed -i '/^KBUILD_.* += -Werror$/,+2d' Makefile

# Install files required for building external modules (in addition to headers)
KbuildFiles="
	Makefile
	Module.symvers
	arch/%arch_dir/Makefile
	scripts/pnmtologo
	scripts/mod/modpost
	scripts/mkmakefile
	scripts/mkversion
	scripts/link-vmlinux.sh
	scripts/mod/mk_elfconfig
	scripts/kconfig/conf
	scripts/mkcompile_h
	scripts/makelst
	scripts/Makefile.*
	scripts/Makefile
	scripts/modules-check.sh
	scripts/Kbuild.include
	scripts/kallsyms
	scripts/genksyms/genksyms
	scripts/basic/fixdep
	scripts/basic/hash
	scripts/extract-ikconfig
	scripts/conmakehash
	scripts/checkversion.pl
	scripts/checkincludes.pl
	scripts/checkconfig.pl
	scripts/bin2c
	scripts/gcc-version.sh
	scripts/gcc-goto.sh
	scripts/module.lds
	scripts/recordmcount.pl
	scripts/recordmcount.h
	scripts/recordmcount.c
	scripts/recordmcount
	scripts/gcc-x86_*-has-stack-protector.sh
	scripts/module-common.lds
	scripts/subarch.include
	scripts/depmod.sh
	scripts/gcc-plugins/*.so
	scripts/ld-version.sh
	scripts/pahole-flags.sh
	scripts/check-local-export
	tools/objtool/objtool

	.config
	.kernelrelease
	gcc_version.inc
	System.map
"
for f in $KbuildFiles; do
	[ -e "$f" ] || continue
	[ -x "$f" ] && mode=755 || mode=644
	install -Dp -m$mode "$f" %buildroot%kbuild_dir/"$f"
done

# Fix symlinks to kernel sources in /lib/modules
rm -f %buildroot%modules_dir/{build,source}
ln -s %kbuild_dir %buildroot%modules_dir/build

# Provide kbuild directory with old name (without %%krelease)
ln -s "$(relative %kbuild_dir %old_kbuild_dir)" %buildroot%old_kbuild_dir

# Provide kernel headers for userspace
%make_build headers_install INSTALL_HDR_PATH=%buildroot%kheaders_dir

#provide symlink to autoconf.h for back compat
pushd %buildroot%old_kbuild_dir/include/linux
ln -s ../generated/autoconf.h
ln -s ../generated/utsrelease.h
ln -s ../generated/uapi/linux/version.h
popd

# remove *.bin files
rm -f %buildroot%modules_dir/modules.{alias,dep,symbols,builtin}.bin
touch %buildroot%modules_dir/modules.{alias,dep,symbols,builtin}.bin
touch %buildroot%modules_dir/modules.{alias,dep,devname,softdep,symbols}

# install documentation
%if_enabled docs
install -d %buildroot%_docdir/kernel-doc-%base_flavour-%version/
cp -a Documentation/* %buildroot%_docdir/kernel-doc-%base_flavour-%version/
%endif # if_enabled docs

# On some architectures (at least ppc64le) kernel image is ELF and
# eu-findtextrel will fail if it is not a DSO or PIE.
%add_verify_elf_skiplist /boot/vmlinuz-*

%define _unpackaged_files_terminate_build 1

%check
banner check
KernelVer=%kversion-%flavour-%krelease
mkdir -p test
cd test
msg='Booted successfully'
%__cc %optflags -s -static -xc -o init - <<__EOF__
#include <unistd.h>
#include <sys/reboot.h>
int main()
{
	static const char msg[] = "$msg\n";
	write(2, msg, sizeof(msg) - 1);
	reboot(RB_POWER_OFF);
	pause();
}
__EOF__
echo init | cpio -H newc -o | gzip -9n > initrd.img
qemu_arch=%_arch
qemu_opts="-machine accel=tcg,type=virt -cpu cortex-a57 -drive if=pflash,unit=0,format=raw,readonly=on,file=%_datadir/AAVMF/QEMU_EFI-pflash.raw"
timeout --foreground 6000 qemu-system-"$qemu_arch" $qemu_opts -kernel %buildroot/boot/vmlinuz-$KernelVer -nographic -append console="$console" -initrd initrd.img > boot.log &&
grep -q "^$msg" boot.log &&
grep -qE '^(\[ *[0-9]+\.[0-9]+\] *)?reboot: Power down' boot.log || {
	cat >&2 boot.log
	echo >&2 'Marker not found'
	exit 1
}

%files
/boot/vmlinuz-%kversion-%flavour-%krelease
/boot/System.map-%kversion-%flavour-%krelease
/boot/config-%kversion-%flavour-%krelease
%dir %modules_dir/
%defattr(0600,root,root,0700)
%modules_dir/*
%exclude %modules_dir/build
%ghost %modules_dir/modules.alias.bin
%ghost %modules_dir/modules.dep.bin
%ghost %modules_dir/modules.symbols.bin
%ghost %modules_dir/modules.builtin.bin
/boot/devicetree/%kversion-%flavour-%krelease

%if_enabled domU
%files -n kernel-image-domU-%flavour
/boot/vmlinux-%kversion-%flavour-%krelease
%endif

%files -n kernel-headers-%flavour
%kheaders_dir

%files -n kernel-headers-modules-%flavour
%kbuild_dir
%old_kbuild_dir
%dir %modules_dir/
%modules_dir/build

%if_enabled docs
%files -n kernel-doc-%base_flavour
%doc %_docdir/kernel-doc-%base_flavour-%version
%endif

%changelog
* Mon Nov 04 2024 Nazarov Denis <nenderus@altlinux.org> 6.6.54-alt1
- Initial build for ALT Linux

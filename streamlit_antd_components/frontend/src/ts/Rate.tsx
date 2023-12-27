import {Streamlit} from "streamlit-component-lib";
import React, {useEffect, useRef, useState} from "react";
import {Rate, ConfigProvider} from 'antd';
import {parseIcon, LabelComponent, GetColor, LightenColor} from "../js/utils.react"
import {StarFilled} from '@ant-design/icons';


interface RateProp {
    label: any
    value: any
    count: any
    symbol: any
    align: string
    position: string
    clear: boolean
    half: boolean
    readonly: boolean
    size: number
    color: any
    stValue: any
}

const AntdRate = (props: RateProp) => {
    //get data
    const label = props['label'];
    const value = props['value'];
    const count = props['count'];
    const symbol = parseIcon(props['symbol']);
    const align = props['align'];
    const position = props['position'];
    const clear = props['clear'];
    const half = props['half'];
    const readonly = props['readonly'];
    const size = props['size'];
    const color = props['color'];
    const primaryColor = GetColor(color == null ? '--primary-color' : color)
    const textColor = GetColor('--text-color')

    const [v, setV] = useState(value)
    // component height
    useEffect(() => Streamlit.setFrameHeight())

    //callback
    const onChange = (value: number) => {
        Streamlit.setComponentValue(value)
    }

    //listen index
    const prevStValue = useRef(props['stValue'])
    useEffect(() => {
        const st_i = props['stValue']
        if (String(st_i) !== String(prevStValue.current)) {
            setV(st_i);
            prevStValue.current = props['stValue']
        }
    }, [props])

    return (
        <ConfigProvider
            theme={{
                components: {
                    Rate: {
                        colorFillContent: LightenColor(textColor, 0.7),
                    },
                },
            }}
        >
            <LabelComponent
                label={label}
                align={align}
                position={position}
                children={
                    <Rate
                        defaultValue={value}
                        value={v}
                        count={count}
                        character={symbol !== null ? symbol : <StarFilled/>}
                        allowClear={clear}
                        allowHalf={half}
                        disabled={readonly}
                        style={{fontSize: size, color: primaryColor}}
                        onChange={onChange}
                    />
                }
            />
        </ConfigProvider>
    );
};

export default AntdRate

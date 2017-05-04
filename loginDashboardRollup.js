
var manager = new RollupManager);

manager.addRollupRule{
    //name,description,pre,post中描述了Rollup的基本属性，在IDE中，选中Rollup行，在下方的Rollup面板中可以看到，便于用户了解该Rollup.
    name: 'loginCommandsRollup',   //Rollup的名字，在引入该Rollup时使用
    description: 'Combine login commands.', //描述，介绍该Rollup的功能
    pre: 'The Dashboard works.The username and password is correct.',//执行该Rollup的前提条件
    post:'The user login Dashboard successfully.',//执行该Rollup的结果
    args: [],
    commandMatchers: [],
    getExpandedCommands: functionargs) {

        var commands = [];  //定义一个Rollup包含的Step列表

        //如下为Rollup包含的Step，按照顺序，依次被执行，每个Step包含三个字段command、target、value,在此不再赘述啦.
        commands.push{
            command: 'open',
            target: '/',
            value: ''
        });

        commands.push{
            command: 'clickAndWait',
            target: 'link=登入',
            value: ''
        });

        commands.push{
            command: 'type',
            target: 'id=username',
            value: '*************'
        });

        commands.push{
            command: 'type',
            target: 'id=password',
            value: '************'
        });

        commands.push{
            command: 'click',
            target: 'id=loginBtn',
            value: ''
        });

        return commands;
    }
});




